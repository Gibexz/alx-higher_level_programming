#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    dict = {}
    for k, v in a_dictionary.items():
        dict[k] = 2 * v
    return dict
