#!/usr/bin/python3
class MyList(list):
    """Class MyList hereda of List"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
