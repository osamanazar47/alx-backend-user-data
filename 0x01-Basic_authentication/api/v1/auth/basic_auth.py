#!/usr/bin/env python3
"""Module for the authentication in the app using basic auth"""
from flask import request
from typing import List, TypeVar
from .auth import Auth


class BasicAuth(Auth):
    """class for authentication using basic auth"""
    