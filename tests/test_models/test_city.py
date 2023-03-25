#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.state = State()

    def test_state_id(self):
        """ """
        new = self.value()
        new.state = self.state
        new.state_id = new.state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = "Nametest"
        self.assertEqual(type(new.name), str)
