#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import type_storage


class Review(BaseModel, Base):
    """Review classto store review information"""

    __tablename__ = "reviews"
    if type_storage == "db":
        text = (
            Column(String(1024), nullable=False)
        )
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        @classmethod
        def set_variables(cls):
            default_dict = {}.fromkeys(["text", "place_id", "user_id"], "")
            for key, val in default_dict.items():
                setattr(cls, key, val)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.text = ""
            self.place_id = ""
            self.user_id = ""
