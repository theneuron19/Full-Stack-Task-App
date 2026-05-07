from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from agent import AgentController
import models
from models import TaskResponse
from database import engine, SessionLocal , get_db
from typing import List

models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
agent = AgentController()

app = FastAPI(
    title="Agent Task Processor",
    description="A simple API to process tasks using an agent and store execution history.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tasks", response_model=TaskResponse)
def create_task(payload: dict, db: Session = Depends(get_db)):
    user_input = payload.get("task")
    result, tool_name, steps = agent.process(user_input)
    
    new_task = models.TaskRecord(
        input_text=user_input,
        output_text=result,
        tool_used=tool_name,
        steps=steps
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks", response_model=List[TaskResponse])
def get_history(db: Session = Depends(get_db)):
    return db.query(models.TaskRecord).order_by(models.TaskRecord.timestamp.desc()).all()