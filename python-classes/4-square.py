#!/usr/bin/python3
"""Defining class"""
class Square:
    """Initializing the values"""
    def __init__(self, size=0):
        self.size = size
        """returning a function and value"""

    def size(self):
        return self.__size
    """Value of the function"""
                
    def size(self, value):
        """running the function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

