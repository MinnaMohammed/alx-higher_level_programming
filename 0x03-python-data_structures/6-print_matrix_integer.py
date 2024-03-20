#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end="")
            if idx < len(row) - 1:
                print(" ", end="")
            idx += 1
        idx = 0
        print()
