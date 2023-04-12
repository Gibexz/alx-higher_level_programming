#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""
module 10-square.py
"""


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
