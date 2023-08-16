#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    test = {}
    for i in a_dictionary:
        test[i] = a_dictionary[i] * 2
    return test
