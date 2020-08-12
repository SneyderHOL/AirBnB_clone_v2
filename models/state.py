#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        cities = self.cities

    @property
    def cities(self):
        """ getter method for cities"""
        cities_list = []
        from models import storage
        dictionary = storage.all(City)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.state_id:
                    cities_list.append(v)
        return cities_list
