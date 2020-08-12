#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Table


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Amenity(BaseModel, Base):
    """ Amenity Class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary=place_amenity,
                                   backref='amenities', viewonly=False)
