#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()
    length = len(matrix)

    for i in range(length):
        newMatrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (newMatrix)
