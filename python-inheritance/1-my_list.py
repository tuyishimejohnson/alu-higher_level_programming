#!/usr/bin/python3
"""Starting a class"""


class MyList(list):
    """Defining the method of a class attributes"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
