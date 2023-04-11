#!/usr/bin/python3
"""
module 1-my_list.py
"""


class MyList(list):
    """
    This inherits from list()
    """
    def print_sorted(self):
        """
        Prints the sorted list
        """
        print(sorted(self))
