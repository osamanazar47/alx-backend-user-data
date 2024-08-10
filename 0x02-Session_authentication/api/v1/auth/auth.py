#!/usr/bin/env python3
"""Module for the authentication in the app"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Defining class Auth for app authentication"""
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """returns a boolean"""
        if path is None:
            return True

        # Check if excluded_paths is None or empty
        if not excluded_paths:
            return True

        # Check if the path is in excluded_paths
        path_with_slash = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if path_with_slash.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """checks the authorization in the header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None for now"""
        return None

    def session_cookie(self, request=None) -> str:
        """Returns a cookie value from a request"""
        if request is None:
            return None
        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
