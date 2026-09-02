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
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

jwt = JWTManager(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask JWT API is running!"
    }), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if email != "user@example.com" or password != "password123":
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    access_token = create_access_token(identity=email)

    return jsonify({
        "access_token": access_token
    }), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()

    return jsonify({
        "logged_in_as": current_user
    }), 200


if __name__ == "__main__":
    app.run(debug=True)