#!/usr/bin/python3
"""
module: rectangle.py
"""

from models.base import Base


class Rectangle(Base):
    """ 
    Rectangle class 

    args:
        width (int), height (int)
        x (int): x coords of the Rectangle
        y (int): y coords of the Rectangle

    Error/Raises:
        TypeError: if x || y || height || width is not int
        ValueError: if x or y is < 0 || if height or width is <= 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter method"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter method"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, yy):
        """y setter method"""
        if type(yy) != int:
            raise TypeError("y must be an integer")
        if yy < 0:
            raise ValueError("y must be >= 0")
        self.__y = yy
