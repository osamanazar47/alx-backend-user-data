#!/usr/bin/env python3
"""module for the authentication"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """for hashing password using bcrypt"""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed