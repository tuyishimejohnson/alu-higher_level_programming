#!/usr/bin/python3
"""Importing a json function"""


import json
"""Defining a function to write an object"""
def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
