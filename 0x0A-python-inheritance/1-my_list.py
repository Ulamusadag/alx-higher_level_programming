#!/usr/bin/python3
"""class description"""


class MyList(list):
    """class"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def print_sorted(self):
        """print sorted"""
        print(sorted(self))


