#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(argv, filename):
    """
        adds items json
    """
    try:
        my_json = load_from_json_file(filename)
    except BaseException:
        my_json = []

    for word in argv:
        my_json.append(word)
    save_to_json_file(my_json, filename)


if __name__ == "__main__":
    argv = argv[1:]
    filename = "add_item.json"
    add_item(argv, filename)
