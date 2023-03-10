from typing import ValuesView
from app.db import Base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import validates, relationship
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
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
    
    # validation for passwords
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 5
        # below encrypts password
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    # below verifies the password
    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )


