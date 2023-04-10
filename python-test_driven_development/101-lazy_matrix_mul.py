#!/usr/bin/python3
""" Importing a numpy as np"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Product of the two matrices.

    Raises:
        TypeError: If the input matrices are not two-dimensional.
        ValueError: If the input matrices cannot be multiplied.

    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        np_result = np.dot(np_a, np_b)
        return np_result.tolist()
    except ValueError:
        raise ValueError("matrices are not aligned")
    except TypeError:
        raise TypeError("inputs must be two-dimensional lists of integers")

