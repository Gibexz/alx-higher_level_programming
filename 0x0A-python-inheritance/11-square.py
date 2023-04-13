#!/usr/bin/python3
"""
module 11-square.py
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class thats inherits Rectangle class
    which inherits BaseGreometry class
    """
    def __init__(self, size):
        """ Constructor """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ square area """
        return super().area()

    def __str__(self):
        """
        str print for Square class
        """
        return f"[Square] {self.__size}/{self.__size}"
