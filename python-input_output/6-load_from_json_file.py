#!/usr/bin/python3
"""Importing a json file"""


import json

def load_from_json_file(filename):
    """Defining a function to create an object"""
    with open(filename) as f:
        data = json.load(f)
    return data
