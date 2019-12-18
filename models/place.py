#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Interger, String, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60),
                     nullable=False,
                     ForeignKey("cities.id"))

    user_id = Column(String(60),
                     nullable=False,
                     ForeignKey("user.id"))

    name = Column(String(128),
                  nullable=False)

    description = Column(String(1024),
                         nullable=True)

    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)

    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)

    max_guest = Column(Integer,
                       nullable=False,
                       default=0)

    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)

    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []

    """ CHILD OF USER """
    """ user = relationship("User","""
    """              backref=backref("places", cascade="all, delete-orphan"))"""
    """ CHILD OF CITIES"""
    """cities = relationship("City", """
    """                      backref=backref, cascade="all, delete-orphan"))"""
    """ place_amenity = Table("""
    """    "place_amenity","""
    """    Base.metadata,"""
    """    Column('place_id',"""
    """        String(60),"""
    """     primary_key=True,"""
    """           ForeignKey("place.id"),"""
    """           nullable=False),"""
    """    Column('amenity_id',"""
    """           String(60),"""
    """           primary_key=True,"""
    """           ForeignKey("amenty.id"),"""
    """           nullable=False)"""
    """)"""
