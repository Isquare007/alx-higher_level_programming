#!/usr/bin/python3
# 1-square.py
"""Represent a class of square that defines a square"""


class Square:
    def __init__(self, size=0):
        """Initializes the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("sizze can not be less than 0")
        self.__size = size
