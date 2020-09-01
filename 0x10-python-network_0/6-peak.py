#!/usr/bin/python3
"""Module is document"""

def find_peak(value):
    '''
        Finds the pick in a list of numbers
    '''
    if value:
        value.sort()
        return value[-1]
