from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "message": "Flask API is running on Vercel!"
    }), 200


@app.get("/test")
def test():
    return jsonify({
        "message": "Test endpoint is working!"
    }), 200