#!/usr/bin/python3
"""Logs HTTPS requests"""
from sys import stdin


def print_log(str_output, obj, size):
    """
    print_log - prints out http log
    str_output: str
    obj: dictionary
    size: int
    """
    lint = sorted([int(x) for x in obj.keys()])
    print(str_output.format(size))
    for k in lint:
        if obj[str(k)] != 0:
            print("{}: {}".format(k, obj[str(k)]))


def run():
    """
    Heart of the code
    """
    str_output = 'File size: {}'
    t_size, idx = 0, 0
    status_c = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
    }

    try:
        for line in stdin:
            if (idx == 10):
                print_log(str_output, status_c, t_size)
                idx = 1
            else:
                idx += 1
            try:
                ln = [line.split()]
                t_size += int(ln[0][-1])
                status_c[ln[0][-2]] += 1
            except Exception:
                pass
        print_log(str_output, status_c, t_size)
    except KeyboardInterrupt:
        print_log(str_output, status_c, t_size)


if __name__ == '__main__':
    """
    I have spent so much time on this HTTP log script
    """
    run()
