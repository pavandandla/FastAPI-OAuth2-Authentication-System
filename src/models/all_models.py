from sqlalchemy import Column, Integer, String
from config.database import Base

class Users(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String(100), unique=True, nullable=False)  
    email=Column(String(100), unique=True, nullable=False)  # New column for GitHub ID
    name = Column(String(100), nullable=False)
