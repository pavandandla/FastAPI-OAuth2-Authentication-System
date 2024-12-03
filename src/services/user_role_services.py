from fastapi import FastAPI, Request, Depends, Query
from fastapi.responses import RedirectResponse
from google.auth.transport.requests import Request as GoogleRequest  # Rename this import to avoid conflict
from google.oauth2 import id_token
from sqlalchemy.orm import Session
from config.config import OAuthConfig
from models.all_models import Users
from jose import jwt
from google_auth_oauthlib.flow import Flow
from config.database import get_db
from config.database import SessionLocal
from authlib.integrations.starlette_client import OAuth 
import os
#from middlewares import create_access_token

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SECRET_KEY = os.getenv('SECRET_KEY')  # Use a secure secret key
ALGORITHM = "HS256"  # or another algorithm if preferred
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

# JWT creation function
async def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# GitHub OAuth setup
oauth = OAuth()

# GitHub OAuth setup
oauth.register(
    name='github',
    client_id=OAuthConfig.GITHUB_CLIENT_ID,
    client_secret=OAuthConfig.GITHUB_CLIENT_SECRET,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    access_token_params=None,
    access_token_url='https://github.com/login/oauth/access_token',
    redirect_uri = 'http://127.0.0.1:8000/github_callback',
    client_kwargs={'scope': 'user:email'},
)

flow = Flow.from_client_secrets_file(
    client_secrets_file=OAuthConfig.CLIENT_SECRETS_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:8000/gmail_callback"
)

async def gmail_login_intiate():
   
    authorization_url, state = flow.authorization_url()
    return RedirectResponse(url=authorization_url)
    
async def gmail_handle_callback(request: Request, db: Session = Depends(get_db)):
    print("Hi mama")
    print("db object:", db)  # Check if db is an instance of Session
    flow.fetch_token(authorization_response=str(request.url))

    # Get the credentials from the flow
    credentials = flow.credentials

    # Use the renamed GoogleRequest to avoid conflict
    id_info = id_token.verify_oauth2_token(
        credentials.id_token,
        GoogleRequest(),  # Use the GoogleRequest class here
        OAuthConfig.GOOGLE_CLIENT_ID,
    )

    # Extract user information from the id_token
    print(id_info)
    login_id = id_info.get("sub")
    name = id_info.get("name")
    email= id_info.get("email")
    print("CHECKMAMA",type(db))
    # Check if user already exists in the table
    user = db.query(Users).filter_by(email=email).first()
    if user:
        return {"message":"Already registered."}
    else:
        # If user does not exist, create a new user
        user = Users(login_id=login_id, email=email, name=name)
        db.add(user)
        db.commit()
        print("SAREMAMA")
        token = await create_access_token({"sub": login_id})

        # Return the token or redirect
    
        return {"message": "Login successful", "token": token}

async def gmail_logout_user():
    # Handle logout functionality as needed
    return {"message": "Logged out successfully"}

async def github_login_initiate(request: Request):
    #print("hello")
    redirect_uri = "http://127.0.0.1:8000/github_callback"
    #print("mama")
    return await oauth.github.authorize_redirect(request, redirect_uri)


async def github_handle_callback(request: Request, db: Session = Depends(get_db)):
    # Fetch the access token using the authorization code
    #print("HICICHHA")
    # Fetch the access token using the authorization code
    token = await oauth.github.authorize_access_token(request)
    #print("Token fetched:", token)  # Debugging

    # Fetch the user information using the access token object
    user_info_response = await oauth.github.get('https://api.github.com/user', token=token)
    user_info = user_info_response.json()  # Convert response to JSON
    print("User info as JSON:", user_info)  # Debugging
    
    # Extract user information
    login_id = user_info.get('id')
    name = user_info.get('name')
    email= user_info.get('email')


    # Check if the user already exists in the database
    user = db.query(Users).filter(Users.login_id == login_id).first()
    if user:
        return {"message":"Already registered."}
    else:
        # If user does not exist, create a new one
        user = Users(login_id=login_id, email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)

        token = await create_access_token({"sub": login_id})

        return {"message": "Login successful", "token": token}


async def github_logout_user():
    # Implement your logout logic if necessary
    return {"message": "Logged out successfully"}