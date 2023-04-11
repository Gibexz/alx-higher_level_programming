#!/usr/bin/python3

"""
module 2-is_same_class.py
"""
def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False

    args:
        obj = the object
        a_class = the class
    """
    return type(obj) == a_class
