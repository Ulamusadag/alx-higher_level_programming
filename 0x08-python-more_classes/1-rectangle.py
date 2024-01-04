#!/usr/bin/python3

""" define rectangular """


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle

        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(valuse, int):
            raise TypeError("width must be an intiger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value