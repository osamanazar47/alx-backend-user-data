#!/usr/bin/env python3
"""Module for the authentication in the app using
basic auth"""
from flask import request
from typing import List, TypeVar
from .auth import Auth


class BasicAuth(Auth):
    """class for authentication using basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 part of the Authorization header"""
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
