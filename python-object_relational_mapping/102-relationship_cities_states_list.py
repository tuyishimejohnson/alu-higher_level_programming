#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Script arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, db_name),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Session handling
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to list all City objects with their associated State
    query = session.query(City).order_by(City.id).all()

    # Results printing
    for city in query:
        print("{}: {} -> {}".format(
            city.id, city.name, city.state.name
        ))
