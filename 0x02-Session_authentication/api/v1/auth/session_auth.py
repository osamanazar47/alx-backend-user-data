#!/usr/bin/env python3
"""Module for the authentication in the app using
session authentication"""
from flask import request
from typing import List, TypeVar
from .auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """Defining the class for Session auth"""
    pass
