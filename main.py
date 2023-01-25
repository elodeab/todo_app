from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from uuid import UUID

## DB 
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

## DB 
models.Base.metadata.create_all(bind=engine)

def get_db():
    
    try:
        db = SessionLocal()
        yield db
        
    finally:
        db.close()

class Todo(BaseModel):
    text:str = Field(min_length=3)
    status:str = Field(min_length=1,max_length=100)
    user:str = Field(min_length=1,max_length=100)

@app.get("/")
def read_api(db:Session = Depends(get_db)):
    return db.query(models.Todos).all()

@app.post("/")
def create_todo(todo:Todo, db:Session = Depends(get_db)):

    todo_model = models.Todos()
    
    todo_model.text = todo.title
    todo_model.status = todo.author
    todo_model.user = todo.description
    
    db.add(todo_model)
    db.commit()
    
    return todo

@app.put("/{todo_id}")
def update_todo(todo_id:int, todo:Todo, db:Session=Depends(get_db)):
    
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    
    if todo_model is None:

        raise HTTPException(
        status_code = 404,
        detail = f"ID {todo_id} does not exist.")
        
    todo_model.title = todo.title
    todo_model.author = todo.author
    todo_model.description = todo.description
    todo_model.rating = todo.rating
    
    db.add(todo_model)
    db.commit()
    
    return todo
