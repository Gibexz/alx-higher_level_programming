#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
module 9-rectangle
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits BaseGreometry
    """
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ str magic print """
        return (f"[Rectangle]  {self.__width}/{self.__height}")
