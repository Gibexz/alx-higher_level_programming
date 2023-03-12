#!/usr/bin/python3

def max_integer(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return None
    my_list.sort()
    leng1 = leng - 1
    return(my_list[leng1])
