
import datetime
from email.policy import default
from typing import ValuesView
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class ToDo(Base):
    
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable = False)
    descr = Column(String(500), nullable = False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)    
    user_id = Column(Integer, ForeignKey('users.id'))