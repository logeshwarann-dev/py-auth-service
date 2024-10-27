from app import db

class Users(db.Model):
    __tablename__ = 'users'  # Explicitly naming the table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
