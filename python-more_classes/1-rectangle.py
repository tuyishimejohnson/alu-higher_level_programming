#!/usr/bin/python3
"""Defining a class"""
class Rectangle:
    """Initializing the method with attribute"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """Returning one of the attributes"""
    def width(self):
        return self._width

    @width.setter
    """Starting the statements"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

