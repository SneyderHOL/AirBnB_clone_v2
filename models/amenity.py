#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Table


class Amenity(BaseModel, Base):
    """ Amenity Class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
