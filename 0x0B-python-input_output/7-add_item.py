#!/usr/bin/python3
"""
module: 7-add_item.py
"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    args = sys.argv[1:]

    file1 = "add_item.json"

    if path.exists(file1):
        jsonList = load_from_jsom_file(file1)
    else:
        jsonList = list()

    save_to_json_file(jsonList + args, file1)
    print(end="")
