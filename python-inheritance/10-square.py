#!usr/bin/python3
"""Defining a rectangle class"""


class Rectangle:
    """Initializing the values of Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # Other methods related to Rectangle class

"""Defining class Square"""


class Square(Rectangle):
    """Initializing the values of Square"""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __repr__(self):
        return f'Square({self.__size})'


class ValidationError(Exception):
    pass


def integer_validator(name, value):
    if not isinstance(value, int):
        raise ValidationError(f'{name} must be an integer')
    if value <= 0:
        raise ValidationError(f'{name} must be a positive integer')
