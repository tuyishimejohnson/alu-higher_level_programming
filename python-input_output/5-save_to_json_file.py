#!/usr/bin/python3
""" save a file to json """
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation """
    with open(filename, 'w') as b:
        b.write(json.dumps(my_obj))
