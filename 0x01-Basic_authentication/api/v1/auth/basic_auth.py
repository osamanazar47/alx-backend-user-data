#!/usr/bin/env python3
"""Module for the authentication in the app using
basic auth"""
from flask import request
from typing import List, TypeVar
from .auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str,
                                           ) -> str:
        """Returns the decoded value of a base64 string"""
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password
