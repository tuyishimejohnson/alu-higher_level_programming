#!/usr/bin/python3
"""Class square"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' implement area '''
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
