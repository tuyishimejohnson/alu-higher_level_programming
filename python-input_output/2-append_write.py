#!/usr/bin/python3
"""Defining a function to append"""


def append_write(filename="", text=""):
    """Returning the number of characters"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
