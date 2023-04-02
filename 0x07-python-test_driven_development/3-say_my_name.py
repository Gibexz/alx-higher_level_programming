#!/usr/bin/python3

"""
This module contains a fuctions that prints:
    My name is <first name> <last name>
    where firstname and lastname are args in the funtion

"""
def say_my_name(first_name, last_name=""):
    """
    Funtion to print a name
    
    Args:
    firstname && lastname: strings expected as input

    Return: Nothing. Prints to stdout

    Raises:
    TypeError:
        if args are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
