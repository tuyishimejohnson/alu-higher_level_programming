#!/usr/bin/python3
"""Defining Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' implement area '''
        return self.__size * self.__size
