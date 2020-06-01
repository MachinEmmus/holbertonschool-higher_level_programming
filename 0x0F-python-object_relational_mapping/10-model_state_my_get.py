#!/usr/bin/python3
"""
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    query = session.query(State).filter(State.name == argv[4]).all()
    if query:
        for _row in query:
            print("{}".format(_row.id))
    else:
        print("Not found")
    session.close()
