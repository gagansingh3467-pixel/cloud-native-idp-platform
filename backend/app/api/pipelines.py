from fastapi import APIRouter, HTTPException
from app.core.database import SessionLocal
from app.modules.cicd.models import Pipeline

router = APIRouter()

@router.get("/pipelines")
def list_pipelines():
    db = SessionLocal()
    pipelines = db.query(Pipeline).all()
    db.close()

    return [
        {
            "id": p.id,
            "repository": p.repository,
            "status": p.status
        }
        for p in pipelines
    ]


@router.get("/pipelines/{pipeline_id}")
def get_pipeline(pipeline_id: int):
    db = SessionLocal()
    pipeline = db.query(Pipeline).get(pipeline_id)
    db.close()

    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")

    return {
        "id": pipeline.id,
        "repository": pipeline.repository,
        "status": pipeline.status,
        "logs": pipeline.logs
    }
