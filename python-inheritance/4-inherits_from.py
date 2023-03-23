#!/usr/bin/python3
"""Initializing a function"""


def inherits_from(obj, a_class):
    """Return true if subclass and attribute is False"""
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
