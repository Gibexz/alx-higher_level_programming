#!/usr/bin/python3
"""
module: 11-student.py
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

    def to_json(self, attrs=None):
        """
        method: retrieves a dictionary representation of Student
        with filter
        """
        if isinstance(attrs, list):
            if all((isintance, str) for att in attrs):
                ret = {}
                for i in attrs:
                    if i in self.__dict__:
                        ret[i] = self.__dict__[i]
                return ret
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:
        """
        for i in json:
            self.__dict__[i] = json[i]
