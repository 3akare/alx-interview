#!/usr/bin/python3
"""
This script logs https requests
"""


if __name__ == "__main__":
    str_output = 'File size: {}'
    t_size = 0
    idx = 0
    status_c = {
        '200': 0, '301': 0,
        '400': 0, '401': 0,
        '403': 0, '404': 0,
        '405': 0, '500': 0
    }

    try:
        while True:
            line = input()
            if (idx == 10):
                print(str_output.format(t_size))
                for k, v in status_c.items():
                    if v != 0:
                        print(f'{k}: {v}')
                idx = 1
            else:
                idx += 1
            ln = [line.split()]
            try:
                t_size += int(ln[0][-1])
            except (IndexError, ValueError):
                pass

            try:
                status_c[ln[0][-2]] += 1
            except Exception:
                pass
        print(str_output.format(t_size))
        for k, v in status_c.items():
            if v != 0:
                print(f'{k}: {v}')
    except KeyboardInterrupt:
        print(str_output.format(t_size))
        for k, v in status_c.items():
            if v != 0:
                print(f'{k}: {v}')
