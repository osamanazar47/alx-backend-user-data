#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from typing import TypeVar
from user import User

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """for adding a user to the db"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """for finding User objects in the db"""
        if not kwargs:
            raise InvalidRequestError()

        try:
            query = self._session.query(User)
            for key, value in kwargs.items():
                if not hasattr(User, key):
                    raise InvalidRequestError(f"Invalid field: {key}")
                query = query.filter(getattr(User, key) == value)

            user = query.one_or_none()
            if user is None:
                raise NoResultFound("No user found matching the criteria")

        except Exception as e:
            raise InvalidRequestError(f"An error occurred: {str(e)}")

        return user
    