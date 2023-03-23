#!/usr/bin/python3
"""Creating a function of integer list"""


def pascal_triangle(n):
    """Returning an empty list"""
    for i in range(n):
        if n <= 0:
            return []
