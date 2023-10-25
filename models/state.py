#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage, type_storage
from models.city import City


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"
    if type_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all,delete")
    else:
        name = ""

        @property
        def cities(self):
            return [city for city in storage.all(cls=City).values()
                    if city.state_id == self.id]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # default_dict = {}.fromkeys(['name'], "")
        # default_dict.update(kwargs)
        # self.__dict__.update(default_dict)

        # if type_storage != "db":
