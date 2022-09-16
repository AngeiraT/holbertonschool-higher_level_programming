#!/usr/bin/python3
from termios import IEXTEN


def square_matrix_simple(matrix=[]):
    new_matrix= []
    for row in matrix:
        new_matrix.append([value**2 for value in row])
    return new_matrix
