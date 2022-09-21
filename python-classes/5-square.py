#!/usr/bin/python3


" Write a class Square that defines a square by: (based on 0-square.py) "


from lib2to3.pgen2.token import EQUAL


class Square:
    """
    Square class

    Attributes:
        size (int) : Private instance attribute, size of the square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """
    Public instance method that returns the current square area
    """
    def area(self):
        return self.__size ** 2

    """
    Public instance method that prints in stdout the square with the character #
    """
    def my_print(self):
        if self._size == 0:
            print()
        for i in range(0, self._size):
            print("#" * self.__size)
