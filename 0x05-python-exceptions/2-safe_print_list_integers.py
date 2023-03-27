#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    b = 0

    for i in range(x):
    #while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            b += 1
        except (ValueError, TypeError):
            pass

    print()
    return b

