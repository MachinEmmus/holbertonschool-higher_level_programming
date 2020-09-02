#!/usr/bin/python3
""" Module Documentation"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = "http://0.0.0.0:5000/search_user"
        load = {}

        if argv[1]:
            load['q'] = argv[1]
        else:
            load['q'] = ""

        r = requests.post(url, data=load)
        r.raise_for_status()

        try:
            obj = r.json()
            try:
                _id = "[{}] ".format(obj['id'])
                name = "{}".format(obj['name'])
                print(_id + name)
            except:
                print('No result')
        except:
            print('Not a valid JSON')
    print('No result')
