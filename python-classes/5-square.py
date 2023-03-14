#!/usr/bin/python3
"""First class"""


class Square:
    """Presenting a square"""

    def __init__(self, size):
        """Initialize a new square value
        Args:
            size (int): The size of the new square value"""
        self.size = size

    @property
    def size(self):
        """gettingthe size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for b in range(0, self.__size):
            [print("#", end="") for d in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
