#!/usr/bin/python3

def element_at(my_list, idx):
    leng = len(my_list) - 1
    if idx > leng:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
