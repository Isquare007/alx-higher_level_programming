#!/usr/bin/python3
"""A square class that defines a square"""


class Square:
    """Represent a square"""
    def __init__(self, size):
        """Initialize a square.
        Args:
            size (int): the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
