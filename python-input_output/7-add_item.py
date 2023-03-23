#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
"""Importing json files and load to it"""
if __name__ == '__main__':
    filename = "add_item.json"

    if not path.exists(filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write("[]")

    my_list = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)

