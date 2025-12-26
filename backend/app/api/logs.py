from fastapi import APIRouter
from datetime import datetime
from app.core.opensearch import client

router = APIRouter(prefix="/logs", tags=["logs"])

@router.post("/ingest")
def ingest_log(payload: dict):
    """
    Expected payload:
    {
      "service": "backend|worker|gateway",
      "level": "INFO|ERROR|DEBUG",
      "message": "text",
      "pipeline_id": 123
    }
    """
    service = payload.get("service", "unknown")
    index_name = f"{service}-logs-{datetime.utcnow().strftime('%Y.%m.%d')}"

    document = {
        "timestamp": datetime.utcnow().isoformat(),
        "service": service,
        "level": payload.get("level", "INFO"),
        "message": payload.get("message", ""),
        "pipeline_id": payload.get("pipeline_id")
    }

    client.index(index=index_name, body=document)
    return {"status": "indexed", "index": index_name}
