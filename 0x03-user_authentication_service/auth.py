#!/usr/bin/env python3
"""module for the authentication"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user to the db"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_pass = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashed_pass)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials"""
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)

            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except Exception:
            # Return False if any exception occurs (e.g., user not found)
            return False

    def create_session(self, email: str) -> str:
        """creates and returns a session id"""
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            self._db._session.commit()
            return user.session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """"Returns the corresponding user to the session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destory_session(self, user_id: int) -> None:
        """destroys the session of given user"""
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
        except NoResultFound:
            return
        return None


def _hash_password(password: str) -> bytes:
    """for hashing password using bcrypt"""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """Returns the string representation of uuid"""
    return str(uuid.uuid4())
