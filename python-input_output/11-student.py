#!/usr/bin/python3
"""Defining a student class"""


class Student:
    """Initializing the values of a student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)

    def __repr__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.age)
