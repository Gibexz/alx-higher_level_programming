#!/usr/bin/python3
"""
module: 8-class_to_json.py
"""


def class_to_json(obj):
    """
     function that returns the dictionary description with simple data
     structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object:
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
