#!/usr/bin/python3
"""Initializing a function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
