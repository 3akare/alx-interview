#!/usr/bin/python3
'''
validUTF8 function module
'''

import re


def validUTF8(data):
    '''
    validUTF8 function
    '''

    regex = [
            r'[\x00-\x7F]',
            r'[\xC2-\xDF][\x80-\xBF]',
            r'[\xE0][\xA0-\xBF][\x80-\xBF]',
            r'[\xE1-\xEC\xEE\xEF][\x80-\xBF]{2}',
            r'\xED[\x80-\x9F][\x80-\xBF]',
            r'\xF0[\x90-\xBF][\x80-\xBF]{2}',
            r'\xF1-\xF3][\x80-\xBF]{3}',
            r'\xF4[\x80-\x8F][\x80-\xBF]{2}'
        ]
    for d in data:
        status = False
        byte = chr(d).encode('utf-8').decode('utf-8')
        for r in regex:
            regex_obj = re.compile(r)
            if (regex_obj.match(byte)):
                status = True
    return status
