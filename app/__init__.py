import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from sqlalchemy.exc import OperationalError
from flask_cors import CORS

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app) 


    # Retry logic for database connection
    retries = 5
    while retries:
        try:
            with app.app_context():
                db.create_all()  # Create tables
                print("Database connected and tables created successfully!")
            break
        except OperationalError:
            retries -= 1
            print("Database connection failed, retrying...")
            time.sleep(2)
    
    if retries == 0:
        print("Failed to connect to the database after several attempts.")
        exit(1)

    # Import routes here to avoid circular imports
    from app.routes import create_routes
    create_routes(app)

    return app
