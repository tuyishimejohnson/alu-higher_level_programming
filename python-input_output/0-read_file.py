#!/usr/bin/python3
"""Define a fuction that reads files"""


def read_file(filename=""):
    """a fuction to read text """
    with open(filename, 'r', encoding='UTF8') as b:
        print(b.read(), end='')
