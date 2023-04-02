#!/usr/bin/python3
"""
This module prints a square with the character #

"""
def print_square(size):
    """
    Function that prints a square with the characte #
    
    Args: size - size of square to be printed

    Returns: Nothing. Prints to stdout
    
    Raises:
    TypeError:
        if size is not an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print('#' * size)
        i += 1
