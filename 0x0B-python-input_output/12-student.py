#!/usr/bin/python3


class Student:
    """MY CLASS STUDENT"""

    def __init__(self, first_name, last_name, age):
        """Initialiazing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    my_dict = self.__dict__
                    continue
                try:
                    my_dict[i] = getattr(self, i)
                except BaseException:
                    pass
        else:
            my_dict = self.__dict__
        return my_dict
