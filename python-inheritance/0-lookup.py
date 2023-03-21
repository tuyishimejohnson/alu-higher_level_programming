#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    attributes = []
    for attr in dir(obj):
        # exclude private and built-in attributes
        if not attr.startswith('_'):
            attributes.append(attr)
    return attributes

