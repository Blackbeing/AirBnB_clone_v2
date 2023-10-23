#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship(
        "Place", back_populates="cities", cascade="all, delete"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_dict = {}.fromkeys(["name", "state_id"], "")
        default_dict.update(kwargs)
        self.__dict__.update(default_dict)
