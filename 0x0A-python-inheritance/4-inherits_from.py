#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Is a class"""
    if issubclass(type(obj), a_class) and not isinstance(obj, a_class):
        return True
    else:
        return False