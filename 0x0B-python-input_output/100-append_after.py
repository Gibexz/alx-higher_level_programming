#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function to 'inserts new_string to a file,
    after find containing search_string
    """
    with open(filename, mode="r+", encoding="utf-8") as afile:
        lines = afile.readlines()
        newCon = []
        for i in range(len(lines)):
            newCon.append(lines[i])
            if search_string in lines[i]:
                newCon.append(new_string)

        afile.seek(0)
        afile.write("".join(newCon))
