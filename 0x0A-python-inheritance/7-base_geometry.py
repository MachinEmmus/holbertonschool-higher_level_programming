#!/usr/bin/python3
class BaseGeometry:
    """Class"""
    def area(self):
        """No create method area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validator if is integer allowed"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
