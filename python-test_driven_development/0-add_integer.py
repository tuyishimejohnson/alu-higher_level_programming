#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns the addition of two integers a and b.

    Args:
        a: An integer or float number.
        b: An integer or float number. Defaults to 98.

    Returns:
        An integer: the addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
