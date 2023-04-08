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
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    if not factors:
        return 0
    return sum(factors)
