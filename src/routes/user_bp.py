from fastapi import APIRouter
from controllers.user_controller import (
    index,
    gmail_login,
    gmail_callback,
    gmail_logout,
    github_login,
    github_callback,
    github_logout,
)

# Create a FastAPI APIRouter
user_bp = APIRouter()

# Define routes
user_bp.add_api_route("/", index, methods=["GET"])
user_bp.add_api_route("/gmail_login", gmail_login, methods=["GET"])
user_bp.add_api_route("/gmail_callback", gmail_callback, methods=["GET", "POST"])
user_bp.add_api_route("/gmail_logout", gmail_logout, methods=["POST"])
user_bp.add_api_route("/github_login", github_login, methods=["GET"])
user_bp.add_api_route("/github_callback", github_callback, methods=["GET", "POST"])
user_bp.add_api_route("/github_logout", github_logout, methods=["POST"])
#user_bp.add_api_route("/protected_area", protected_area, methods=["GET"])
