#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="places")
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    cities = relationship("City")
    reviews = relationship(
        "Review", back_populates="place", cascade="all, delete"
    )
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_dict = {}.fromkeys([
            "city_id",
            "user_id",
            "name",
            "description",
            ], "")
        default_dict.update({}.fromkeys([
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            ], 0)
        )
        default_dict.update({}.fromkeys([
            "longitude",
            "latitude",
            ], 0.0)
        )
        default_dict["amenity_ids"] = []
        default_dict.update(kwargs)
        self.__dict__.update(default_dict)
