#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, scoped_session

env = os.environ


class DBStorage:
    """This class manages storage of hbnb models in database"""

    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        username = env.get("HBNB_MYSQL_USER", "hbnb_dev")
        passwd = env.get("HBNB_MYSQL_PWD", "hbnb_dev_pwd")
        host = env.get("HBNB_MYSQL_HOST", "localhost")
        db = env.get("HBNB_MYSQL_DB", "hbnb_dev_db")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                username, passwd, host, db
            ),
            pool_pre_ping=True,
            future=True,
        )

        if env.get("HBNB_ENV", "dev") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    @property
    def objects(self):
        return self.all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        tables_dict = {
            "users": User,
            "places": Place,
            "states": State,
            "cities": City,
            "amenities": Amenity,
            "reviews": Review,
        }

        if cls is None:
            for k, v in tables_dict.items():
                try:
                    objs = self.__session().query(v).all()
                    for obj in objs:
                        key_id = f"{obj.__class__.__name__}.{obj.id}"
                        self.__objects[key_id] = obj
                except exc.ArgumentError:
                    pass
        else:
            klass = (
                classes.get(cls, None)
                if isinstance(cls, str)
                else classes.get(str(cls.__name__), None)
            )
            if klass is None:
                return self.__objects
            else:
                try:
                    objs = self.__session().query(klass).all()
                    for obj in objs:
                        key_id = f"{obj.__class__.__name__}.{obj.id}"
                        self.__objects[key_id] = obj
                except exc.ArgumentError:
                    pass

        return self.__objects

    def new(self, obj):
        """Adds new object to storage db"""
        self.__session().add(obj)

    def save(self):
        """Saves storage dictionary to db"""
        # with self.__session() as session:
        self.__session().commit()

    def reload(self):
        """Loads storage dictionary from db"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        Base.metadata.create_all(bind=self.__engine)

        session_factory = sessionmaker(
            self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

    def delete(self, obj=None):
        """
        Delete object from db
        """
        if obj is not None:
            self.__session().delete(obj)

    def close(self):
        """Close current session"""
        self.__session().close()
