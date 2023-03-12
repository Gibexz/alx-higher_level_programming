#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        # mylist = my_list.reverse()
        # print(mylist) this prints none which is not iterable
        for i in reversed(my_list):
            print("{:d}".format(i))
