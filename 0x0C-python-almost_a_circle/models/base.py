#!/usr/bin/python3
""" Base Class """

import json
import os


class Base:
    """My class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """My init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialization a json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file in the cls"""
        with open(cls.__name__ + ".json", "w") as f:
            my_list = []
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    my_list.append(i.to_dictionary())
                list_in_json = cls.to_json_string(my_list)
            return f.write(list_in_json)
