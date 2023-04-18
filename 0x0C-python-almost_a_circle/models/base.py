#!/usr/bin/python3
"""
Module: base.py
"""

import json


class Base:
    """
    “base” of all other classes in this project
    goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        args:
            list_objs:  a list of instances who inherits of Base
                        for eg, rectangle and square instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_dict = cls(1, 1)
            else:
                dummy_dict = cls(1)
            dummy_dict.update(**dictionary)
            return dummy_dict

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                lst_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in lst_dict]
        except IOError:
            return []
