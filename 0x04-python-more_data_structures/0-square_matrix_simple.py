#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            new_matrix[row][col] = (matrix[row][col] * matrix[row][col])
    return new_matrix
