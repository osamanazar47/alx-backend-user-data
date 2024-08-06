#!/usr/bin/env python3
"""Module for the authentication in the app"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None for now"""
        return None
