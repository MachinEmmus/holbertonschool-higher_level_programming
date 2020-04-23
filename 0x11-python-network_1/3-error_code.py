#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print(data.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
