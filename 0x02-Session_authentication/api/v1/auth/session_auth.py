#!/usr/bin/env python3
"""Module for the authentication in the app using
session authentication"""
from flask import request
from typing import List, TypeVar
from .auth import Auth
import base64
from models.user import User
import uuid


class SessionAuth(Auth):
    """Defining the class for Session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method for creating the session object that
        stores the session info"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
