from fastapi import FastAPI, HTTPException
from models import Todos, User, Status
from typing import List
from uuid import uuid4

app = FastAPI()

user = User(
    id=uuid4(),
         first_name="John",
         last_name="Doe",
         email="john.doe@example.com"
        )

db: List[Todos] = [
    Todos(
        id=uuid4(),
        title="Homework",
        text="Doing homework",
        completed = Status.doing,
        owner = user
    )
]

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/api/v1/todos")
def get_all_todos():
    return db
