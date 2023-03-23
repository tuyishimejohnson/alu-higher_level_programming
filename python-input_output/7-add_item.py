#!/usr/bin/python3
"""Importing a function from a json file"""


from json import dumps

"""Defining a function to add arguments"""
def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
