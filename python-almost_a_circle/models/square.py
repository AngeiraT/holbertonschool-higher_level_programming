#!/usr/bin/pyhton3
"""
Module for the class Square
Task 10: Write the class Square that inherits from Rectangle
"""


from ctypes import sizeof
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class Square
    size, x, y = private instance attribute

    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor Square
        Call the super class with id, x, y, width and height - 
        this super call will use the logic of the __init__ of the Rectangle class. 
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size property getter
        Returns: private instance attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter but unsing the attribute of Rectangle:
        - first width because we want the error validation of its
        """
        self.width = value
        self.height = value
    