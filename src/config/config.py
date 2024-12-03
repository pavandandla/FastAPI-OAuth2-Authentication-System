import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()  # Ensure mysqlclient works with pymysql
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Allow HTTP traffic for local dev

load_dotenv()  # Load environment variables from a .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM = 'HS256'  # Algorithm for JWT
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # e.g. "mysql+pymysql://username:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class OAuthConfig:
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    CLIENT_SECRETS_FILE = os.path.join(os.path.dirname(__file__), "client_secret.json")
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
