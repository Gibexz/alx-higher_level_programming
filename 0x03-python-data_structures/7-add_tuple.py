#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0

    if len(tuple_a) < 1:
        pass
    elif len(tuple_a) < 2:
        a0 = tuple_a[0]
    else:
         a0 = tuple_a[0]
         a1 = tuple_a[1]


    if len(tuple_b) < 1:
        pass
    elif len(tuple_b) < 2:
        b0 = tuple_b[0]
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    i = a0 + b0
    j = a1 + b1

    return (i, j)
