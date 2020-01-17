#!/usr/bin/python3
def remove_char_at(str, n):
    str_new, count = "", 0 
    for i in str:
        if count == n:
            pass
        else:
            str_new = str_new + i
        count += 1
    return str_new
