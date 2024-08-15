#!/usr/bin/env python3
"""Module for a basic flask app"""
from flask import Flask, jsonify, request, abort
import flask
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

@app.route('/sessions', methods=['POST'],
           strict_slashes=False)
def login():
    """for checking the login of the user"""
    data = request.form
    email = data.get('email')
    password = data.get('password')
    if email is None or password is None:
        abort(401)
    if not AUTH.valid_login(email=email, password=password):
        abort(401)
    session_id = AUTH.create_session(email=email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", value=session_id)
    return res, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
