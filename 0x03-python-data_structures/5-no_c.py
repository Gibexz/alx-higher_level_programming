#!/usr/bin/python

def no_c(my_string):
    newString = ""
    for char in my_string:
        if char not in 'cC':
            newString += char

    return newString
