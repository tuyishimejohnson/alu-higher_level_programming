#!/usr/bin/python3
"""A base class for geometry objects"""
class BaseGeometry:
    """Calculates the area of geometry
    Raises:Exception: If the method is not implemented in subclass"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer input value.

        Args:
        name (str): The name of the value.
        value (int): The value to validate.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
