#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
