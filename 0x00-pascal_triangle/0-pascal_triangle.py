#!/usr/bin/python3
''' Techincal Interview: Pascal's Triangle'''


def factorial(n):

    '''
        factorial - return the factorial of a number
        n: integer
        return: integer
    '''
    factor = 1
    while n != 0:
        factor *= n
        n -= 1
    return factor


def pascal_triangle(n):

    '''
        pascal_triangle - returns a list of lists of integers
        representing the Pascal's triangle of n
        n: integer
        return: a list of list
    '''
    if n <= 0:
        return []
    iArray, oArray = [], []
    for i in range(n):
        for j in range(i + 1):
            value = factorial(i)//(factorial(j)*factorial(i-j))
            iArray.append(value)
        oArray.append(iArray)
        iArray = []
    return oArray
