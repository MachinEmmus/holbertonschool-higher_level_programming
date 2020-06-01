#!/usr/bin/python3
""" Python ORM create table states"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """ This is the table in SQL State but with ORM"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=True)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
