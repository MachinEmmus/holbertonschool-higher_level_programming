#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    query = session.query(City, State).filter(State.id == City.state_id)\
                                      .order_by(City.id).all()
    for row, row_1 in query:
        print("{}: {} -> {}".format(row.id, row.name, row_1.name))
    session.close()
