#!/usr/bin/python3
"""Defining a class"""


class LockedClass(object):
    """using a builtin function to prevent creating new instance attributes"""
    __slots__ = 'first_name'
