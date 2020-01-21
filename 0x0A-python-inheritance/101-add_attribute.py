#!/usr/bin/python3
def add_attribute(instance, name, value):
    if hasattr(instance, name):
        raise TypeError("can't add new attribute")
    instance.name = value
