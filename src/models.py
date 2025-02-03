import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    full_name = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship('Favorite', backref='user',lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(String(100), nullable=False)
    rotation_period = Column(String(100), nullable=False)
    orbital_period = Column(String(100), nullable=False)
    gravity = Column(String(100), nullable=False)
    population = Column(String(100), nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(100), nullable=False)
    eye_color = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    hair_color = Column(String(100), nullable=False)
    height = Column(String(20), nullable=False)
    mass = Column(String(40), nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld = Column(String(40), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    length = Column(String(100), nullable=False)
    cost_in_credits = Column(String(100), nullable=False)
    crew = Column(String(100), nullable=False)
    max_atmosphering_speed = Column(String(100), nullable=False)
    cargo_capacity = Column(String(100), nullable=False)
    consumables = Column(String(100), nullable=False)

class Film(Base):
    __tablename__ = 'film'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String(80), nullable=False)
    character = Column(Integer, ForeignKey('character.id'))
    vehicle = Column(Integer, ForeignKey('vehicle.id'))
    planet = Column(Integer, ForeignKey('planet.id'))

class Favorite_vehicle(Base):
    __tablename__ = 'favorite_vehicle'

    id = Column(Integer, primary_key=True)
    vehicle = Column(Integer, ForeignKey('vehicle.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'

    id = Column(Integer, primary_key=True)
    planet = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorite_film(Base):
    __tablename__ = 'favorite_film'

    id = Column(Integer, primary_key=True)
    film = Column(Integer, ForeignKey('film.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorite_character(Base):
    __tablename__ = 'favorite_character'

    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
