#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[i][j] = matrix[i][j] ** 2
    
    return result_matrix
