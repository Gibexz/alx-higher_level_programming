#!/usr/bin/python3
"""
module 8-rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
