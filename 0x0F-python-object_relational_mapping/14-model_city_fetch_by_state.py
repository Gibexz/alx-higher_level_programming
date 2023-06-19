#!/usr/bin/python3
"""
 script that  prints all City objects from the
 database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                )
            )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")

    query = session.query(State, City).\
        filter(City.state_id == State.id).all()

    for row in query:
        print(f"{row[0].name}: ({row[1].id}) {row[1].name}")

    session.close()
