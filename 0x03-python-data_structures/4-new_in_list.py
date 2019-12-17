def new_in_list(my_list, idx, element):
    other_list = my_list.copy()
    if (idx < 0 or idx > len(my_list) -1):
        return other_list
    for i in range(0, len(my_list)):
        if i == idx:
            other_list[i] = element
            return other_list
