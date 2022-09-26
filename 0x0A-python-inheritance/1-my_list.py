#!/usr/bin/python3
"""My list"""


class MyList(list):
    """prints the sorted list"""
    def print_sorted(self):
        llist = sorted(self)
        print(llist)
