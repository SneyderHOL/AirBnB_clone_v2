#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel, Base):
    """ Amenity Class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary="place_amenity",
                                   backref='amenities', viewonly=False)
