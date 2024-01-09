#!/usr/bin/python3
"""function the appends new texxt in already existing files or create a new file"""


def write(filename="", text=""):
    "Return yhe number of the added text

    Args:
        filename (str): the name of the file
        text: (str): the text to be added
    Returns:
        the number of characters
    """
    with open(filename, a, encoding="utf-8") as f:
        return f.write(text)

