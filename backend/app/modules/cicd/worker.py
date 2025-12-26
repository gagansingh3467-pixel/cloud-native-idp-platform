import time
import docker
import requests
from redis.exceptions import ConnectionError

from app.core.redis import redis_client
from app.core.database import SessionLocal
from app.modules.cicd.models import Pipeline

LOG_API = "http://backend:8000/logs/ingest"
DEMO_SERVICE_PATH = "/workspace/idp-demo-service"
docker_client = docker.from_env()

def send_log(service, level, message, pipeline_id=None):
    try:
        requests.post(LOG_API, json={
            "service": service,
            "level": level,
            "message": message,
            "pipeline_id": pipeline_id
        }, timeout=2)
    except Exception:
        pass

def run_worker():
    print("CI/CD Worker started (logging enabled)...")

    while True:
        try:
            job = redis_client.brpop("pipeline_queue", timeout=5)
        except ConnectionError:
            time.sleep(3)
            continue

        if not job:
            continue

        pipeline_id = int(job[1])
        db = SessionLocal()
        pipeline = db.query(Pipeline).get(pipeline_id)

        if not pipeline:
            db.close()
            continue

        try:
            pipeline.status = "RUNNING"
            db.commit()
            send_log("worker", "INFO", "Build started", pipeline_id)

            image, build_logs = docker_client.images.build(
                path=DEMO_SERVICE_PATH,
                tag=f"idp-demo:{pipeline.id}"
            )

            for log in build_logs:
                if "stream" in log:
                    send_log("worker", "INFO", log["stream"], pipeline_id)

            pipeline.status = "SUCCESS"
            db.commit()
            send_log("worker", "INFO", "Build successful", pipeline_id)

        except Exception as e:
            pipeline.status = "FAILED"
            db.commit()
            send_log("worker", "ERROR", str(e), pipeline_id)

        finally:
            db.close()
            time.sleep(1)
