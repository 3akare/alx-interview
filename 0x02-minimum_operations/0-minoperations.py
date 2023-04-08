#!/usr/bin/python3
'''
minimum operations function module
'''


def minOperations(n):
    '''
    minimum operation function
    '''

    if n <= 1:
        return 0
    factors = []
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return sum(factors)
