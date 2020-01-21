#!/usr/bin/python3
class MyInt(int):
    def __init__(self, num):
        self.num = num

    def __ne__(self, value):
        return (self.num == value)

    def __eq__(self, value):
        return (self.num != value)

    def __str__(self):
        return str(self.num)
