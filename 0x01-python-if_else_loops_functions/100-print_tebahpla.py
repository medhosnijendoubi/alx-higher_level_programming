#!/usr/bin/python3
# Author - Mohamed Hosni Jendoubi
""""Print the alphabet in reverse order alternating"""
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
