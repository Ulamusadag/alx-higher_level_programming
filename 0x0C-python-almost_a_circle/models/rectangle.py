#!/usr/bin/python3
"""This rectangle model"""
from models.base import Base

class Rectangle(Base):
    """ This Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the initial constructor

        Args:
            width(int): the width
            height(int): height
            X(int):x
            y(int):y
            id(int): id
        """

        super().__init__(id)

        self._width = width
        self._height = height
        self._x = x
        self._y = y

        @property
        def width(self):
            """getting width"""
            return self._width
        
        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <=0:
                raise ValueError("width must be positive")
            self._width = value

        @property
        def height(self):
            """Getter for the height attribute."""
            return self._height

        @height.setter
        def height(self, value):
            """Setter for the height attribute, ensuring it's a positive integer."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be a positive integer")
            self._height = value

        @property
        def x(self):
            """Getter for the x-coordinate attribute."""
            return self._x

        @x.setter
        def x(self, value):
            """Setter for the x-coordinate attribute, ensuring it's an integer."""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            self._x = value

        @property
        def y(self):
            """Getter for the y-coordinate attribute."""
            return self._y

        @y.setter
        def y(self, value):
            """Setter for the y-coordinate attribute, ensuring it's an integer."""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            self._y = value
