#!/usr/bin/python3
"""
python file that contains the class definition of a
City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(Base):
    """
    This class inherit from Base
    Attributes:
        id that represents a column of an auto-generated,
            unique integer, cant be null and is a primary key
        name represents a column of a string with maximum 128
            characters and cant be null
        state_id that represents a column of an integer
            can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
