#!/usr/bin/python3
"""define an empty class."""


class BaseGeometry:
    """ an empty class"""

    def area(self):
        """Not done."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value.
         Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
