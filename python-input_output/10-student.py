#!/usr/bin/python3
"""Initalizing the function with attributes"""


def to_json(self, attrs=None):
    if attrs is None:
        return self.__dict__
    else:
        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict
