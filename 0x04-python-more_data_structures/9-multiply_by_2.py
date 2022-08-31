#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dictionary  = a_dictionary.copy()
    for k, v in multiply_dictionary.items():
        multiply_dictionary[k] = v * 2
    return multiply_dictionary
