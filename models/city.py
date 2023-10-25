#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import type_storage


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    if type_storage == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        # places = relationship(
        #     "Place", backref="cities", cascade="all,delete"
        # )
    else:
        @classmethod
        def set_variables(cls):
            default_dict = {}.fromkeys(["name", "state_id"], "")
            for key, val in default_dict.items():
                setattr(cls, key, val)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
