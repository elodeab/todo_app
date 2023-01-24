from pydantic import BaseModel
from typing import Optional
from uuid import UUID,uuid4
from enum import Enum

class Status(str,Enum):
    todo="todo"
    doing="doing"
    done="done"

class User(BaseModel):
   id: Optional[UUID] = uuid4()
   first_name:str
   last_name:str
   middle_name: Optional[str]
   
class Todos(BaseModel):
    id = Optional[UUID] = uuid4()
    text:str 
    completed:Status
    owner_id:User
    
