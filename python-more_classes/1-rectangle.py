#!/usr/bin/python3
"""Starting a class"""


class Rectangle:
    """Initializing the attributes"""
    def __init__(self, Rectangle_width=0, Rectangle_height=0):
        self.width = Rectangle_width
        self.height = Rectangle_height

    @property
    def Rectangle_width(self):
        return self.Rectangle_width

    @width.setter
    def Rectangle_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.Rectangle_width = value

    @property
    def Rectangle_height(self):
        return self._height

    @height.setter
    def Rectangle_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.Rectangle_height = value
