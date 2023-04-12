#!/usr/bin/python3
"""
module 101-add_attribute.py
"""


def add_attribute(obj, name, value):
    """ Adds attribute to an object if possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
