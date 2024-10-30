from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db  # Moved db import here to avoid circular import
from app.models import Users
from app.utils import generate_jwt
from flask_cors import cross_origin

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
@cross_origin(origins="*")
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        
        return jsonify({"message": "Username and password are required"}).headers.add('Access-Control-Allow-Origin', '*'), 400

    hashed_password = generate_password_hash(password)
    new_user = Users(username=username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()

    

    return jsonify({"message": "User created successfully"}).headers.add('Access-Control-Allow-Origin', '*'), 201

@auth_bp.route('/login', methods=['POST'])
@cross_origin(origins="*")
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Users.query.filter_by(username=username).first()
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid username or password"}).headers.add('Access-Control-Allow-Origin', '*'), 401

    token = generate_jwt(user.id)
    return jsonify({"token": token}), 200
