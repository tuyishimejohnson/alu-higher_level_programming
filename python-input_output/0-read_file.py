#!/usr/bin/python3
"""Defining a function that reads a file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
