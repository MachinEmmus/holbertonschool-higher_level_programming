#!/usr/bin/python3
""" Python ORM create table cities"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ This is the table in SQL City but with ORM"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)