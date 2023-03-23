#!/usr/bin/python3
"""Defining a class"""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """
        Calculates the area of the geometry object.

        Raises:
        NotImplementedError: If the method is not implemented in a subclass.
        """
        raise Exception("area() is not implemented")
