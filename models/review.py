#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    # place_id = ""
    # user_id = ""
    # text = ""

    """New attrs"""
    __tablename__ = "reviews"
    text = Column(String(length=1024), nullable=False)
    place_id = Column(String(length=60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(length=60), ForeignKey("users.id"), nullable=False)
