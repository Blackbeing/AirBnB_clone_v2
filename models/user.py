#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True, default="")
    last_name = Column(String(128), nullable=True, default="")
    places = relationship(
        "Place", back_populates="user", cascade="all, delete"
    )
    reviews = relationship(
        "Review", back_populates="user", cascade="all, delete"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_dict = {}.fromkeys(
            ["first_name", "last_name", "password", "email"], ""
        )
        default_dict.update(kwargs)
        self.__dict__.update(default_dict)

        # If not kwargs, raise Error, password, email required
        # if kwargs, if pwd or email not aval, raise error <attr> required

        # if not kwargs:
        #     raise ValueError("email and password are required")
        # else:
        #     if "email" not in kwargs:
        #         raise ValueError("email is required")
        #     if "password" not in kwargs:
        #         raise ValueError("password is required")

        #     default_dict = {}.fromkeys(
        #         ["email", "password", "first_name", "last_name"], ""
        #     )
        #     default_dict.update(kwargs)
        #     self.__dict__.update(default_dict)
