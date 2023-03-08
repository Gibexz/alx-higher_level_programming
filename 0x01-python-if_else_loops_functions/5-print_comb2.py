#!/usr/bin/python3

i = 0
while i <= 99:
    if i < 10:
        print("0{0:d}".format(i), end=", ")
    else:
        print("{0:d}".format(i), end=", " if i < 99 else "\n")
    i += 1
