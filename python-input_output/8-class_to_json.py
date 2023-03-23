#!/usr/bin/python3
"""Initialising a function"""


def class_to_json(obj):
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif obj is None:
        return None
    else:
        attributes = {}
        for attribute_name in dir(obj):
            if not attribute_name.startswith("_"):
                attribute_value = getattr(obj, attribute_name)
                attributes[attribute_name] = class_to_json(attribute_value)
        return attributes
