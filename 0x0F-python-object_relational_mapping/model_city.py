#!/usr/bin/python3
"""
python file that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
     Class with table for cities
    """

    __tablename__ = "cities"

    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates='cities')
