#!/usr/bin/python3
"""Importing json and sys from os and typing"""


import json
import sys
from os import path
from typing import List

def save_to_json_file(my_obj: any, filename: str):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename: str):
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

def add_item(argv: List[str]):
    my_list = []
    if path.isfile('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    my_list.extend(argv[1:])
    save_to_json_file(my_list, 'add_item.json')
    return my_list

if __name__ == '__main__':
    print(add_item(sys.argv))
