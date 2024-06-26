#!/usr/bin/python3
""" this is the base model"""

class Base:
    """ this the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the init constructor
        
        Args:
            id(int): can be provided or not
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects 

