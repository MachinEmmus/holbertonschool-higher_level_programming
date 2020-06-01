#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    query = session.query(State, City).join(City).order_by(City.id)
    for _S, _C in query.all():
        print("{}: ({}) {}".format(_S.name, _C.id, _C.name))
    session.close()
