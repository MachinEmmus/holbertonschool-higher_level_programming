def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for i in reversed(range(0, len(my_list))):
            print("{:d}".format(my_list[i]))
