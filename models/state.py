#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_dict = {}.fromkeys(['name'], "")
        default_dict.update(kwargs)
        self.__dict__.update(default_dict)
