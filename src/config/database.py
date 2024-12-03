from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load database URL from environment variables
DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')

# SQLAlchemy engine and session setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#. autocommit=False ensures transactions must be explicitly committed and autoflush prevents sql alchemi automaticcall sinchronizing session with database.
Base = declarative_base()

# Function to initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get a database session for request handling
def get_db():
    db = SessionLocal()
    try:
        yield db  # Yield session to the route handler
    finally:
        db.close()  # Ensure session is closed after the request


"""
The `get_db()` function implements a dependency injection pattern for database sessions. 
It creates a new database session for each request and ensures proper cleanup by closing the session after use. 
The yield statement makes it a dependency generator, allowing FastAPI to manage the session lifecycle automatically. 
This pattern prevents resource leaks and ensures thread-safe database operations.
"""