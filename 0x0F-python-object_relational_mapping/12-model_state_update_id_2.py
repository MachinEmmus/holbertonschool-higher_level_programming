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
    query = session.query(State).filter_by(id=2).first()
    query.name = "New Mexico"
    session.commit()