#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.

        Args:
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
