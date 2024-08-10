#!/usr/bin/env python3
""" Module of session auth views views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from typing import Tuple
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def session_login() -> Tuple[str, int]:
    """"""
    not_found_response = {"error": "no user found for this email"}
    email = request.form.get('email', None)
    passwd = request.form.get('password', None)
    if email is None or email == '':
        return jsonify({ "error": "email missing" }), 400
    if passwd is None or passwd == '':
        return jsonify({ "error": "password missing" }), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify(not_found_response), 404
    if len(users) <= 0:
        return jsonify(not_found_response), 404
    if users[0].is_valid_password(passwd):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401
