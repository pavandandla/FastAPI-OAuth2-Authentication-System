import jwt
from datetime import datetime, timedelta
from config.config import Config
from fastapi import HTTPException
from jose import jwt
from fastapi import Depends
from config.config import OAuthConfig
import os

SECRET_KEY = os.getenv('SECRET_KEY')  # Use a secure secret key
ALGORITHM = "HS256"  # or another algorithm if preferred
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

async def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_token(token):
    try:
        return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token!")

def jwt_required(func):
    async def wrapper(*args, **kwargs):
        auth_header = kwargs.get('authorization')
        if not auth_header:
            raise HTTPException(status_code=403, detail="Token is missing!")
        token = auth_header.split()[1]
        return verify_jwt_token(token)
    return wrapper
