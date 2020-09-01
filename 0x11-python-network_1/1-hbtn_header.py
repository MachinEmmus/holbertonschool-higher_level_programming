#!/usr/bin/python3
""" Module Documentation"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheaders()

    for val in header:
        if val[0] == "X-Request-Id":
            print(val[1])
