from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from routes.user_bp import user_bp
from config.database import init_db
import os

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv('SECRET_KEY')  
    
    # The current CORS configuration is too permissive, 
    # allowing requests from any origin with any method and headers. 
)

# Initialize the database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Include user routes
app.include_router(user_bp)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
