from sqlalchemy import Column,Integer,String
from database import Base

class Todos(Base):
    
    __tablename__ = "todos"
    
    id = Column(Integer,primary_key=True,index=True)
    text = Column(String)
    status = Column(String)
    user = Column(String)
    
    
