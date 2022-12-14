#!/usr/bin/python3
"""
Module for the class Rectangle
Task 2: Write the class Rectangle that inherits from Base
Task 3: Validate the attributes of al setter methods
Task 4: Adding the public method def area that returns the area
        value of the Rectangle instance
Task 5: Update the class Rectangle by adding the public method def display
        (self): that prints in stdout the Rectangle instance with the
        character #

"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    width, height, x, y = private instance attribute

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width property getter

        Returns: private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height property getter

        Return: private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X property getter

        Return: private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y property getter

        Return: private isntance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to calculate the area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Method to display a square of #"""
        for y in range(self.y):
            print()
        for j in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method so that it returns a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Method that assigns update attributes"""
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
