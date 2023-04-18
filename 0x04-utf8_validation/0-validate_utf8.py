#!/usr/bin/python3
'''
validUTF8 function module
'''

import re


def validUTF8(data):
    '''
    validUTF8 function
    '''

    index = 0
    while index < len(data):
        if data[index] > 0b11110000:
            return False
        if data[index] & 0b10000000 == 0b00000000:
            span = 1
        elif data[index] & 0b11100000 == 0b11000000:
            span = 2
        elif data[index] & 0b11110000 == 0b11100000:
            span = 3
        elif data[index] & 0b11111000 == 0b11110000:
            span = 4
        else:
            return False
        if len(data) < index + span:
            return False
        for i in range(index + 1, index + span):
            if data[i] & 0b11000000 != 0b10000000:
                return False
        index += span
    return True
