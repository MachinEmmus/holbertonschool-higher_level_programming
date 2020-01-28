#!/usr/bin/python3
"""
Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """My class Rectangle that inheritance of Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """My init method for parametres and call the init inheritance class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """Get to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to height"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """get to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter to x"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """Get to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter to y"""
        self.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(name, value):
        """Function validate the correct input"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Function thats return the area"""
        return self.__width * self.__height

    def display(self):
        """Function that print my Rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x + "#" * self.width, end="")
            print()

    def __str__(self):
        """My str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update dates"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """My dictyonary"""
        keys = ["id", "width", "height", "x", "y"]
        dicty = {}
        for val in keys:
            dicty[val] = getattr(self, val)
        return dicty
