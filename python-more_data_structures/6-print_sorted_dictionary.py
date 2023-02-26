#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
