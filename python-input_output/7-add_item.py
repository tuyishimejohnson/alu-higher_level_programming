#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a JSON file"""

import json
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == "__main__":
    json_file = "add_item.json"
    args = sys.argv[1:]

    if path.exists(json_file):
        items = load_from_json_file(json_file)
    else:
        items = []

    items.extend(args)
    save_to_json_file(items, json_file)
