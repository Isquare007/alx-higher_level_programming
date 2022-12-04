#!/usr/bin/python3
"""
All states via SQLAlchemy
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    data = session.query(City).order_by(City.id).all()

    for city in data:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()
