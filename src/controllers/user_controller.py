from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.user_role_services import gmail_login_intiate, gmail_handle_callback, gmail_logout_user, github_login_initiate, github_handle_callback, github_logout_user
from config.database import get_db
from sqlalchemy.orm import Session

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

async def gmail_login():
    return await gmail_login_intiate()

async def gmail_callback(request: Request, db: Session = Depends(get_db)):
    return await gmail_handle_callback(request, db)

async def gmail_logout():
    return await gmail_logout_user()

async def github_login(request: Request):
    return await  github_login_initiate(request)

async def github_callback(request: Request, db: Session = Depends(get_db)):
    return await github_handle_callback(request, db)


async def github_logout():
    return await github_logout_user()
