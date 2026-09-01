from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/hello")
def hello():
    return jsonify({
        "message": "Hello from Blueprint!"
    }), 200


@api.get("/students")
def students():
    return jsonify({
        "students": [
            {
                "id": 1,
                "name": "Ravi",
                "course": "Python"
            },
            {
                "id": 2,
                "name": "Kiran",
                "course": "Flask"
            }
        ]
    }), 200