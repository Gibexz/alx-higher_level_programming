#!/usr/bin/python3
"""
module: 10-student.py
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
        with filter
        """
        if attrs is None:
            return self.__dict__
        else:
            ret = {}
            for i in attrs:
                if i in self.__dict__:
                    ret[i] = self.__dict__[i]
            return ret
