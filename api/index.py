# from flask import Flask, jsonify
# from api.routes import api

# app = Flask(__name__)


# @app.get("/")
# def home():
#     return jsonify({
#         "message": "Flask API is running on Vercel!"
#     }), 200


# @app.get("/test")
# def test():
#     return jsonify({
#         "message": "Test endpoint is working!"
#     }), 200


# app.register_blueprint(api, url_prefix="/api")

from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gaddar is superman'
# app.config['expiration_time'] = 3600  # Token expiration time in seconds
jwt = JWTManager(app)
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4ODMzMTY2NSwianRpIjoiMjEzZWEzNzUtYmY5NS00MTg5LThiZGEtOWEzNWUxN2UxYTY1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZXhhbXBsZS5jb20iLCJuYmYiOjE3ODgzMzE2NjUsImNzcmYiOiJhODdhZTk3Ny05ZjMxLTRjYzAtOTQ3OS1hYzZlYTQwMWM0ODQiLCJleHAiOjE3ODgzMzI1NjV9.qFwflgEQMiwmF9Ddo-g96MF1JIk7UYw1gk5WU10KJOQ
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if email !='user@example.com' or password != 'password123':
        return jsonify({'message': 'Invalid email or password'}), 401
    else:
        access_token=create_access_token(identity=email) 
        return jsonify({'access_token': access_token}), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)