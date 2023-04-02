#!/usr/bin/python3
'''
canUnlockAll function module
'''


def canUnlockAll(boxes):
    '''
    canUnlockAll function
    '''

    len_of_box = len(boxes)
    keys = set(boxes[0])

    for box in boxes:
        if box == []:
            keys.add(99)
        for i in box:
            keys.add(i)
    return len(keys) == len_of_box
