#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    find the pick inbetween numbers hint(the largest number between two numbers)
    """
    lent = len(list_of_integers)
    if lent == 0:
        return None
    if list_of_integers is None:
        return None
    if (list_of_integers[lent - 1] == list_of_integers[lent - 2]) :
        return lent - 1
    for x in range(1, lent):
        if ((list_of_integers[x] >= list_of_integers[x - 1]) and
                (list_of_integers[x] > list_of_integers[x + 1])):
            return(list_of_integers[x])
