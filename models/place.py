#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Float, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = self.amenities
        reviews = self.reviews

    @property
    def amenities(self):
        """ getter method for amenities"""
        amenities_list = []
        from models import storage
        dictionary = storage.all(Amenity)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.place_id:
                    amenities_list.append(v)
        return amenities_list

    @amenities.setter
    def amenities(self, value):
        """setter method for amenities"""
        if type(value) != Amenity:
            return
#            raise TypeError('amenities value must be of type Amenity')
        self.amenity_ids.append(value)

    @property
    def reviews(self):
        """ getter method for reviews"""
        reviews_list = []
        from models import storage
        dictionary = storage.all(Review)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.place_id:
                    reviews_list.append(v)
        return reviews_list
