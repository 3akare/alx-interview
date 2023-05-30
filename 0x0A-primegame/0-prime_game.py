#!/usr/bin/python3
'''
Prime Game: Technical Interview
'''    
def isWinner(x, nums):
    number = 0  # or grundy number  
    for ak in range(x):
        number ^= nums[ak % len(nums)];

    return "Ben" if number > 0 else "Maria"

