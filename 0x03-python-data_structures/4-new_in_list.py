#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    leng = len(my_list) - 1
    newList = my_list.copy()
    if idx < 0 or idx > leng:
        return newList
    else:
        newList[idx] = element
        return newList
