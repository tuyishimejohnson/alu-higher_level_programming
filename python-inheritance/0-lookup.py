#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    result = []
    """Working on the argument of the function"""
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            result.append(attr_name + '()')
        else:
            result.append(attr_name)
    return result

