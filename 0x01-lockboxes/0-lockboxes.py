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
    empty = False
    empty_status = 0

    for box in boxes:
        if box == [] or len(box) == 0:
            empty = True
            empty_status += 1
        for i in box:
            keys.add(i)

    for i in range(100):
        if (empty or empty_status != 0):
            if (i not in keys):
                keys.add(i)
                empty_status -= 1
                break
    if (len_of_box < len(keys)):
        return True
    return len(keys) == len_of_box
