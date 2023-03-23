#!/usr/bin/python3
''' a class Student that defines a student'''


class Student:
    '''define a class student '''

    def __init__(self, first_name, last_name, age):
        '''instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method to_json'''
        return self.__dict__
