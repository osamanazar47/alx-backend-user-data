#!/usr/bin/env python3
"""Module for a basic flask app"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'],
           strict_slashes=False)
def home():
    """for the home route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'],
           strict_slashes=False)
def users():
    """for registering users"""
    data = request.form
    email = data.get('email')
    password = data.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({f"email": "{email}", "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
