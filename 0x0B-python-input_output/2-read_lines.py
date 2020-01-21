#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0
    with open('my_file_0.txt') as f:
        for line in f:
            print(line, end="")
            count += 1
            if count == nb_lines:
                break
