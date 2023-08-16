#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    test = 0
    ten = 0
    for tup in my_list:
        test += tup[0] * tup[1]
        ten += tup[1]
    return float(test / ten)
