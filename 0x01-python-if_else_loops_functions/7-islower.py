#!/usr/bin/python3

def islower(c):
    char = ord(c)
    if (char < 97 or char > 122):
        return False
    else:
        return True
