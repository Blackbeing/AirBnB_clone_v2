#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import type_storage as ts


class Review(BaseModel, Base):
    """Review classto store review information"""

    __tablename__ = "reviews"
    text = (
        Column(String(1024), nullable=False)
    )
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    user = relationship("User")
    place = relationship("Place")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.text = ""
            self.place_id = ""
            self.user_id = ""
