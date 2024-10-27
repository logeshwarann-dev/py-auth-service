from flask import Flask
from app.auth import auth_bp

def create_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
