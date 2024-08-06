#!/usr/bin/env python3
"""Module for the authentication in the app"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Defining class Auth for app authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns a boolean"""
        return False

    def authorization_header(self, request=None) -> str:
        """checks the authorization in the header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None for now"""
        return None
