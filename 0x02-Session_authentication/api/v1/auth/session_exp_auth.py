#!/usr/bin/env python3
"""Session authentication with expiration module for the API."""

import os
from flask import request
from datetime import datetime, timedelta

from .session_auth import SessionAuth

class SessionExpAuth(SessionAuth):
    """Session authentication class with expiration."""

    def __init__(self) -> None:
        """Initializes a new SessionExpAuth instance with session duration."""
        super().__init__()
        try:
            self.session_lifetime = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_lifetime = 0

    def create_session(self, user_id=None):
        """Creates a session ID for the specified user.

        Args:
            user_id (str): The user ID for whom the session is being created.

        Returns:
            str: The created session ID, or None if creation fails.
        """
        session_token = super().create_session(user_id)
        if type(session_token) != str:
            return None
        self.user_id_by_session_id[session_token] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return session_token

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to lookup.

        Returns:
            str: The associated user ID, or None if the session is expired or invalid.
        """
        if session_id in self.user_id_by_session_id:
            session_data = self.user_id_by_session_id[session_id]
            if self.session_lifetime <= 0:
                return session_data['user_id']
            if 'created_at' not in session_data:
                return None
            current_time = datetime.now()
            session_duration = timedelta(seconds=self.session_lifetime)
            expiration_time = session_data['created_at'] + session_duration
            if expiration_time < current_time:
                return None
            return session_data['user_id']
        