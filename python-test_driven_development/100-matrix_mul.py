#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b and return the result.

    Args:
    - m_a: a list of lists of integers or floats
    - m_b: a list of lists of integers or floats

    Returns:
    - a list of lists of integers or floats representing the product of m_a and m_b

    Raises:
    - TypeError if m_a or m_b is not a list, or not a list of lists
      or if one element of those list of lists is not an integer or a float
      or if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size)
    - ValueError if m_a or m_b is empty (it means: = [] or = [[]])
      or if m_a and m_b can’t be multiplied

    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]
    """
    # Validate inputs
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) \
            or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute matrix product
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
