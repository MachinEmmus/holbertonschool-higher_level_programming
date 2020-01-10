#!/usr/bin/python3
class Square:
    """
        This is my class Square
    """
    def __init__(self, size=0):
        """
        The init function in my class
        Args:
            size (int): Is the size of my square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
