#!/usr/bin/python3
"""
module 6-base_geometry.py
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Area: raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
