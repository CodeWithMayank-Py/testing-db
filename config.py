import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://default:uH8UWTAP1Bac@ep-lucky-sun-a4jtxgb3-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
