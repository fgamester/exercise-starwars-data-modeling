import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)

    favorites_planets = relationship('Planet', secondary='favorites_planets', back_populates='favorited_by')
    favorites_characters = relationship('Character', secondary='favorites_characters', back_populates='favorited_by')

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)

    favorite_by = relationship('User', secondary='favorites_characters', back_populates='favorites_characters')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)

    favorite_by = relationship('User', secondary='favorites_planets', back_populates='favorites_planets')


class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

class FavoritesCharacters(Base):
    __tablename__ = 'favorites_characters'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
