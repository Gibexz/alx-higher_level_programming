#!/usr/bin/python3
"""
module: 9-student.py
"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method: retrieves a dictionary representation of Student
        """
        return self.__dict__.copy()
