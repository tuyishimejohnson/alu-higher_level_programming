#!/usr/bin/python3
"""Defining a function matrix_mul"""


def matrix_mul(m_a, m_b):
    """validate input matrix m_a"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    num_cols_a = len(m_a[0])
    if not all(len(row) == num_cols_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    """validate input matrix m_b"""

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    num_cols_b = len(m_b[0])
    if not all(len(row) == num_cols_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    """ validate that matrices can be multiplied"""

    if num_cols_a != len(m_b):
        raise ValueError("m_b can't be empty")

    """ multiply matrices"""

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(num_cols_b):
            dot_product = sum(m_a[i][k] * m_b[k][j] for k in range(num_cols_a))
            row.append(dot_product)
        result.append(row)
    return result
