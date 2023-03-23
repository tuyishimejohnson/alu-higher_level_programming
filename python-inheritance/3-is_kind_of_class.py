#!/usr/bin/python3
"""Initializing the function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, the specified class; otherwise False."""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
