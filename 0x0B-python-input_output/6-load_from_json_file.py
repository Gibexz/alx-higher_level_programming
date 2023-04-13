#!/usr/bin/python3
"""
module: 6-load_from_json_file.py
"""

import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”:
    """
    with open(filename, "r") as afile:
        text = json.load(afile)
        return text
