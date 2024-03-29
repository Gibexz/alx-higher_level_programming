#!/usr/bin/python3
"""
This module contains a class that defines a rectangle
"""


class Rectangle():
    """
    class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width property """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height property """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
