from app.db import Base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import validates

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    
    
    # validation for email goes below 
    @validates('email')
    def validate_email(self, key, email):
        # ensure email contains '@'
        assert '@' in email 
        
        return email 

