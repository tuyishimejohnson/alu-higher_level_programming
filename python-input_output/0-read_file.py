#!/usr/bin/python3
"""Defining a function that reads a file"""


def read_file(filename=""):
    """Representing the values of the file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except:
        pass
