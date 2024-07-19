import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print(f"Database URL: {os.environ.get('DATABASE_URL')}")  # Debugging line

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
