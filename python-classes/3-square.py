#!/usr/bin/python3
"""Defining class"""


class Square:
    """initializing the values"""
    def __init__(self, size=0):
        """the methods"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return self.__size ** 2
