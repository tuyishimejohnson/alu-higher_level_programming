#!/usr/bin/python3
"""Starting a class"""
class MyList(list):
    """Defining a class function for sorting"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
