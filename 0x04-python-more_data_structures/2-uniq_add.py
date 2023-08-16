#!/usr/bin/python3
def uniq_add(my_list=[]):
    key = set(my_list)
    test = 0
    for i in key:
        test += i
    return test
