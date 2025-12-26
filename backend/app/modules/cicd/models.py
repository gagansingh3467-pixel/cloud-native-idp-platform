from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    repository = Column(String, index=True)
    status = Column(String, default="QUEUED")
    logs = Column(Text, default="")
