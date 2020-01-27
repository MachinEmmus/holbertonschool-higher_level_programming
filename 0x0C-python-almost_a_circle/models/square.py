#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """My class Square that inhiretance of Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().validate("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)   
    
    def to_dictionary(self):
        keys = ["id", "size", "x", "y"]
        dicty = {}
        for val in keys:
            dicty[val] = getattr(self, val)
        return dicty

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
