from email.policy import default
from typing import ValuesView
from xmlrpc.client import DateTime
from app.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, column_property

class Todo(Base):
    
    __tablename__ = 'todos'
    user = relationship('User')
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable = False)
    descr = Column(String(500), nullable = False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)