#!/usr/bin/python3
"""
module: 5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation:
    """
    """text = json.dumps(my_obj)"""
    with open(filename, mode="w") as afile:
        json.dump(my_obj, afile)
