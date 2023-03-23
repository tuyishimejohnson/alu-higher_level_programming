#!/usr/bin/python3
def class_to_json(obj):
    """Converts an object to a dictionary with simple data types."""
    if isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or obj is None:
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    else:
        return {key: class_to_json(getattr(obj, key)) for key in dir(obj) if not key.startswith('_')}

