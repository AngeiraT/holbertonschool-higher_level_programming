#!/usr/bin/python3
from termios import IEXTEN


def square_matrix_simple(matrix=[]):
    square= []
    for row in matrix:
        square.append([value**2 for value in row])
    return square
