#!/usr/bin/python3
'''
validUTF8 function module
'''

import re


def validUTF8(data):
    '''
    validUTF8 function
    '''

    regex = re.compile(r'^[\x00-\x7F]|\
    [\xC2-\xDF][\x80-\xBF]|\xE0[\xA0-\xBF][\x80-\xBF]|\
    [\xE1-\xEC\xEE\xEF][\x80-\xBF]{2}|\xED[\x80-\x9F][\x80-\xBF]\
    |\xF0[\x90-\xBF][\x80-\xBF]{2}|[\xF1-\xF3][\x80-\xBF]{3}|\xF4[\x80-\x8F]\
    [\x80-\xBF]{2}$')
    status = True
    for d in data:
        byte = chr(d).encode('utf-8').decode('utf-8')
        if (regex.match(byte)):
            pass
        else:
            status = False
    return status
