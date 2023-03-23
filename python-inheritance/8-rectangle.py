#!/usr/bin/python3
"""Class representing a rectangle"""


class Rectangle(BaseGeometry):
    """Initializing a rectangle with height and width"""
    def __init__(self, width, height):
        """Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If the width or height is not an integer.
        ValueError: If the width or height is less than or equal to 0.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        The area of the rectangle.
        """
        return self.__width * self.__height
