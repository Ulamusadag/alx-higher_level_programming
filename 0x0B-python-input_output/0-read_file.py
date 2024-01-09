#!/usr/bin/python3
"""define a function reading a file"""


def read_file(filename=""):
    """print the content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
