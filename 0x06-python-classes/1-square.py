#!/usr/bin/python3
# 1-square.py
"""Represent a class of square that defines a square"""


class Square:
    def __init__(self, size=0):
        """Initializes the square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
