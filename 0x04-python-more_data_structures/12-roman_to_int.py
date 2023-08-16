#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    list_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    test = 0
    for j in range(len(roman_string)):
        if j > 0 and list_roman[roman_string[j]] > list_roman[roman_string[j - 1]]:
            test += list_roman[roman_string[j]] - 2 * \
                        list_roman[roman_string[j - 1]]
        else:
            test += list_roman[roman_string[j]]
    return test
