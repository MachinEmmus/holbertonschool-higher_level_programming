#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of "
if number < 0:
    num = number * -1
else:
    num = number
if ((num % 10) > 5):
    print(s + "{} is {} and is greater than 5".format(number, num % 10))
elif ((num % 10) == 0):
    print(s + "{} is {} and is 0".format(number, num % 10))
else:
    print(s + "{} is {} and is less than 6 and not 0".format(number, num % 10))
