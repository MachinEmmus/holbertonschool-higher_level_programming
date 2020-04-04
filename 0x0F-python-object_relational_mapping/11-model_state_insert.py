#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(con.format(user, passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    instance = session.query(State).filter_by(name="Louisiana").first()
    print(instance.id)
