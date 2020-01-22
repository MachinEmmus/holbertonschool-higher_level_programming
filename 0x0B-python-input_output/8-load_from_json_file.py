#!/usr/bin/python3
from json import loads


def load_from_json_file(filename):
    with open(filename) as f:
        obj = f.read()
        return (loads(obj))
