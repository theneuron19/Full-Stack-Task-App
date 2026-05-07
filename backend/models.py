from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

Base = declarative_base()

class TaskRecord(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String)
    output_text = Column(String)
    tool_used = Column(String)
    steps = Column(JSON)  # Stores the execution trace
    timestamp = Column(DateTime, default=datetime.utcnow)

class TaskResponse(BaseModel):
    id: int
    input_text: str
    output_text: str
    tool_used: str
    steps: List[str]
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True