#!/usr/bin/python3
'''
isWinner() Function
'''


def isWinner(x, nums):
    '''
    isWinner. Declares the winner in a strange game
    '''
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(1 for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)))  # noqa
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
