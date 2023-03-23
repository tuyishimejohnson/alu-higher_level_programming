#!/usr/bin/python3
"""Importing json function"""


import json


def to_json_string(my_obj):
    """Converts the given object to a JSON string.

    Args:
        my_obj: The object to be converted.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
