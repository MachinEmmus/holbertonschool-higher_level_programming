#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        count = f.write(text)
    return count
