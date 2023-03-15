#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix1 = []
    for row in matrix:
        newrow = list(map(lambda x: x ** 2, row))
        matrix1.append(newrow)
    return matrix1
