#!/usr/bin/python3
"""
python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This class inherit from Base
    Attributes:
        id that represents a column of an auto-generated,
            unique integer, cant be null and is a primary key
        name represents a column of a string with maximum 128
            characters and cant be null
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
