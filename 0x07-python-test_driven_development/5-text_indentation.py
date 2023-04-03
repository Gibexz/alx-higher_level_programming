#!/usr/bin/python3
"""
This module contains only a function that prints a text
with 2 new lines after each of these characters: ., ? and :

"""
def text_indentation(text):
    """
    The indentation function.

    args: text to be indented

    returns: Nothing. Prints to stdout

    raise: TypeError - if text is not of type str

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    copy = text[:]
    

    for c in ".?:":
        copy_text = copy.split(c)
        copy = ""
        for i in copy_text:
            i = i.strip(" ")
            copy = i + c if copy == "" else copy + "\n\n" + i + c
    
    print(copy[:-3], end="")

