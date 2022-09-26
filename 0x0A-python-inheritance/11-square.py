#!/usr/bin/python
"""A square class"""


Rectangle = __import__('9-Rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        """initialize the value"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__self, self.__self)

    def __str__(self):
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
