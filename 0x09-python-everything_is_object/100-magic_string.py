#!/usr/bin/python3
var = 0
def magic_string():
    global var
    return (("Holberton, " * (var + var += 1))[: -2])
