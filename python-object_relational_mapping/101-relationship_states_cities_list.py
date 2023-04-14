#!/usr/bin/env python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa sorted in ascending order
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Connection setup to the database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(mysql_username, mysql_password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session instance
    session = Session()

    # Retrieve all the states sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state and their corresponding cities sorted by id
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
