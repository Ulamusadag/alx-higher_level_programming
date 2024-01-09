#!/usr/bin/python3
"""Define a function that write to file"""


def write_file(filename="", text=""):
    """Degine a function that return c

    Args:
        filname (str): the file
        text (str):text
    Returns:
        number of c
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
