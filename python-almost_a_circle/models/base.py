#!/usr/bin/python3
"""
Module for the class Base
Task 1 : Write the first class Base with a private class attribute
"""


class Base:
    """
    Class Base
    nb_objects = private class attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
