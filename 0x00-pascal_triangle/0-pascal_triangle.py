#!/usr/bin/python3
''' Techincal Interview: Pascal's Triangle'''
from math import factorial


def pascal_triangle(n):
    '''
        pascal_triangle - returns a list of lists of integers
        representing the Pascal's triangle of n
        n: integer
        return: a list of list
    '''

    try:
        if n <= 0:
            return []
        iArray, oArray = [], []
        for i in range(n):
            for j in range(i + 1):
                # nCr of each row and store in a list ie. n!/(n-r)!r!.
                # In the case i!//(i - j)!*j!
                value = factorial(i)//(factorial(j)*factorial(i-j))
                iArray.append(value)
            oArray.append(iArray)
            iArray = []
        return oArray
    except Exception:
        pass
