#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for i in matrix:
        list(map(lambda x: x ** 2, i))
    return matrix
