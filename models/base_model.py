#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, String
from datetime import datetime
from copy import copy
from models import type_storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {
                "id": str(uuid.uuid4()),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            }
        else:
            kwargs.pop("__class__", None)
            kwargs['id'] = kwargs.get('id', str(uuid.uuid4()))
            kwargs["created_at"] = datetime.fromisoformat(
                kwargs.get("created_at", datetime.utcnow().isoformat())
            )
            kwargs["updated_at"] = datetime.fromisoformat(
                kwargs.get("updated_at", datetime.utcnow().isoformat())
            )
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update(
            {"__class__": (str(type(self)).split(".")[-1]).split("'")[0]}
        )
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """
        Delete object from storage
        """
        from models import storage

        key_id = f"{self.__class__.__name__}.{self.id}"
        storage.pop(key_id, None)
