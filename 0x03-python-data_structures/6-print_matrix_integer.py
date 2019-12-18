#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for i, num in enumerate(rows):
            print("{:d}".format(num), end="")
            if (i < len(rows) - 1):
                print("{}".format(" "), end="")
        print()
