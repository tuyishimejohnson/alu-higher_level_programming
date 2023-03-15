#!/usr/bin/python3
"""Starting a class"""


class Rectangle:
    """Representing the attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.height):
                for j in range(self.width):
                    rectangle += "#"
                if i != self.height - 1:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
