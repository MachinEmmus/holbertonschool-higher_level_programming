#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Is a class"""
    return True if isinstance(obj, a_class) and type(obj) != a_class else False
