
from email.policy import default
from typing import ValuesView
from datetime import datetime
from app.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ToDo(Base):
    
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable = False)
    descr = Column(String(500), nullable = False)
    created_at = Column(datetime, default = datetime.utcnow())
    
