#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ module write_file """
    with open(filename, 'w') as b:
        return b.write(text)
