#!/usr/bin/python3
class Square:
    """
    This class defines a square.

    Attributes:
        side (int or float): The length of each side of the square.

    Methods:
        perimeter(): Returns the perimeter of the square.
        area(): Returns the area of the square.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Square class.

        Args:
            side (int or float): The length of each side of the square.
        """
        self.side = side

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            The perimeter of the square.
        """
        return 4 * self.side

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.side ** 2

