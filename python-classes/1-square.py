#!/usr/bin/python3
" Write a class Square that defines a square by: (based on 0-square.py) "

class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with size (no type/value verification)
        - You are not allowed to import any module"""
    def __init__(self, size):
        """Size is a private attributte:
        The size of a square is crucial for a square"""
        self._size = size
