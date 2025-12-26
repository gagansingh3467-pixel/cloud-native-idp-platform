from fastapi import APIRouter, Request
from app.core.database import SessionLocal
from app.modules.cicd.models import Pipeline
from app.core.redis import redis_client

router = APIRouter()

@router.post("/github")
async def github_webhook(request: Request):
    payload = await request.json()
    repo = payload.get("repository", {}).get("full_name")

    db = SessionLocal()
    pipeline = Pipeline(repository=repo, status="QUEUED")
    db.add(pipeline)
    db.commit()
    db.refresh(pipeline)
    db.close()

    redis_client.lpush("pipeline_queue", pipeline.id)

    return {
        "message": "Pipeline queued",
        "pipeline_id": pipeline.id,
        "status": pipeline.status
    }
