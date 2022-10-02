#!/usr/bin/python3
"""Base class"""


class Base:
    """Represent a base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base. args id(int): identity of new base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


