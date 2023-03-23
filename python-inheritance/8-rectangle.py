#!/usr/bin/python3
"""Defining a BaseGeometry class"""


class BaseGeometry:
    """Initializing items in area"""
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} height must be an integer")
        if value <= 0:
            raise ValueError(f"{name} width must be greater than 0")

"""Defining a Rectangle class"""


class Rectangle(BaseGeometry):
    """Initializing the values in Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__heiight)
