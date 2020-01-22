#!/usr/bin/python3
def class_to_json(obj):
    return (getattr(obj, "__dict__"))
