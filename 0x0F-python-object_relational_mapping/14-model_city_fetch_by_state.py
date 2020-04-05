#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(con.format(user, passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    for sta, cit in session.query(State, City).all():
        print("{}: ({}) {}".format(sta.name, cit.id, cit.name))
