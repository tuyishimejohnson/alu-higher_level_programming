#!/usr/bin/python3
"""Defining a Student class"""


class Student:
    """Initializing the values of the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }
