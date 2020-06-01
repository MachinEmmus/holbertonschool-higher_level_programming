#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    query = session.query(State).order_by(State.id).all()
    for _row1 in query:
        print("{}: {}".format(_row1.id, _row1.name))
        for _row in _row1.cities:
            print("    {}: {}".format(_row.id, _row.name))
    session.close()
