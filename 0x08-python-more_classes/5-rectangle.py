#!/usr/bin/python3
"""
This module contains a class that defines a rectangle
"""


class Rectangle():
    """
    class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return (self.__height * self.width)

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """ Return string which prints the rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        """ Had two Errors. Will not identify it
        temp = []
        for i in range(self.height):
            temp.append('#' * self.width)
            temp.append('\n')
        return ''.join(temp)
        """
        temp = ''
        for co in range(self.height):
            for ro in range(self.width):
                temp += '#'
            if co != self.height - 1:
                temp += '\n'
        return temp

    def __repr__(self):
        """
        Return a string representation of the rectangle to
        be able to recreate a new instance by using eval()
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ Destructor method """
        print('Bye rectangle...')
