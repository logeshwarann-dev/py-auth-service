import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'BitsPilani'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@db:5432/auth_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
