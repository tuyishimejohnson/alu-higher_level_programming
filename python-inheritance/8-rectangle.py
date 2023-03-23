#!/usr/bin/python3
"""Defining a class BaseGeometry"""


class BaseGeometry:
    """Initializing the items in area"""
    def area(self):
        raise NotImplementedError()

    def perimeter(self):
        raise NotImplementedError()

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""Defining a class Rectangle"""


class Rectangle(BaseGeometry):
    """Initializing the items in Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
