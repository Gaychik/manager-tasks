from datetime import datetime
from models.models_for_db import *
from fastapi import Depends,Body,APIRouter
from fastapi.responses import JSONResponse


router_t=APIRouter()


@router_t.get("/{id}")
def get_task(id, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task == None:
        return JSONResponse(status_code=404, content={"message": "Task is not found"})
    return task

@router_t.post("/")
def create_task(data=Body(), db: Session = Depends(get_db)):
    task = Task(name=data["name"],
                phone=data["priority"],
                date=datetime.now(),
                priority=data['priority'],
                is_complete=data['is_complete'])
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router_t.put("/")
def edit_task(data=Body(), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == data["id"]).first()
    if task == None:
        return JSONResponse(status_code=404, content={"message": "Task is not found"})
    task.name = data["name"],
    task.phone = data["priority"],
    task.date = datetime.now(),
    task.priority = data['priority'],
    task.is_complete = data['is_complete']
    db.commit()
    db.refresh(task)
    return task


@router_t.delete("/{id}")
def delete_task(id, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task == None:
        return JSONResponse(status_code=404, content={"message":  "Task is not found"})
    db.delete(task)
    db.commit()
    return task