#!/usr/bin/python3
'''
validUTF8 function module
'''

import re


def validUTF8(data):
    '''
    validUTF8 function
    '''

    skip = 0
    for d in data:
        if skip > 0:
            if (d & 0b11000000) != 0b10000000:
                return False
            skip -= 1
            continue
        if (d & 0b10000000) == 0:
            continue
        elif (d & 0b11100000) == 0b11000000:
            skip = 1
        elif (d & 0b11110000) == 0b11100000:
            skip = 2
        elif (d & 0b11111000) == 0b11110000:
            skip = 3
        else:
            return False
    return skip == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
