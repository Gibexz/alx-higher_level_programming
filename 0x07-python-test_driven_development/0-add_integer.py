#!/usr/bin/python3
""" function that adds 2 integers. """

def add_integer(a, b=98):
    """
    args = a and b

    returns
        the sum of a and b
            or
        TypeError if a or b is not an int
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    
    a = int(a)
    b = int(b)
    return a + b
