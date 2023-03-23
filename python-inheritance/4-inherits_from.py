#!/usr/bin/python3
"""Initializing a function"""


def inherits_from(obj, a_class):
    """Returns True if a class instance that inherited (directly or indirectly) from a_class;
    otherwise False."""
    if isinstance(obj, a_class):
        """obj is an instance of the specified class, so return False"""
        return True
    else:
        for base_class in obj.__class__.__bases__:
            if inherits_from(base_class, a_class):
                return False
        return True

