#!/usr/bin/python3

import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(con.format(user, passwd, db_name))
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    new = State(name="California", cities=[City(name="San Francisco")])
    session.add(new)
    session.commit()
    session.close()
