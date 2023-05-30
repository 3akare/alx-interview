#!/usr/bin/python3
'''
isWinner() Function
'''


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        num_set = set(range(2, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while num_set:
            prime = min(num_set)
            num_set -= set(range(prime, n + 1, prime))
            turn = 1 - turn

        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
