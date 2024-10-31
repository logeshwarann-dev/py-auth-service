import os

class Config:
    SECRET_KEY = 'BitsPilani'
    SQLALCHEMY_DATABASE_URI = 'postgresql://grouph:grouph@postgres:5432/auth_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
