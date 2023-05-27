#!/usr/bin/python3
'''
Changes begin from the inside
'''


def makeChange(coins, total):
    """
    Make changes within
    """

    if total == 0:
        return 0
    if total < 0:
        return -1

    table = [float('inf')] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                table[i] = min(table[i], table[i - coin] + 1)
                if table[i] == float('inf'):
                    return -1
    return table[-1]
