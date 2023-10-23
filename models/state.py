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
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all,delete,delete-orphan")

    @property
    def cities(self):
        """Getter method for cities belonging to a state"""
        if type_storage == 'db':
            return self.cities
        else:
            # return [city for city in storage.all(cls=City).items()]
            return [
                city for city_id, city in storage.all(cls=City).items()
                if city.state_id == self.id
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
