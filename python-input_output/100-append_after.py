#!/usr/bin/python3
"""
function that inserts a line of text to a file,\
        after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    '''module Search and update
    '''
    words = ''

    with open(filename, 'r') as dub:
        for line in dub:
            words += line
            if search_string in line:
                words += new_string
    with open(filename, "w") as bi:
        bi.write(words)
