#!/usr/bin/python3
"""
module 2-append_write.py
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        nb_chars = a_file.write(text)
        return nb_chars
