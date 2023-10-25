#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models import type_storage


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    if type_storage == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            "Review", backref="place", cascade="all, delete"
        )
    if type_storage != "db":
        @classmethod
        def init_rows(cls):
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
            for key, val in default_dict.items():
                setattr(cls, key, val)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
