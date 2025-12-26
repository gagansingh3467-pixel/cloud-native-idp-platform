import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.api import webhooks, pipelines, logs
from app.core.database import engine, Base
from app.modules.cicd import models

app = FastAPI(title="Internal Developer Platform")

@app.on_event("startup")
def startup():
    retries = 5
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected successfully")
            return
        except OperationalError:
            print("Database not ready, retrying...")
            retries -= 1
            time.sleep(3)
    raise Exception("Database not reachable after retries")

app.include_router(webhooks.router, prefix="/webhooks")
app.include_router(pipelines.router)
app.include_router(logs.router)

@app.get("/health")
def health():
    return {"status": "ok"}
