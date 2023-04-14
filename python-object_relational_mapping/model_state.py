#!/usr/bin/python3

"""Defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class linked to the 'states' table in the database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Return the string representation of a State instance."""
        return f"State(id={self.id}, name='{self.name}')"
