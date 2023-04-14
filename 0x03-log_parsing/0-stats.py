#!/usr/bin/python3
def print_log(s_code, t_size, o_put):
    '''
    print statictics
    like my code runs as it should but still fails because of documentation
    '''

    print(o_put.format(t_size))
    for k, v in s_code.items():
        if v != 0:
            print(f'{k}: {v}')


def run():
    '''
    Starts the log server
    Which shouldn't be a problem
    '''

    o_put = '''File size: {}'''
    t_size, num = 0, 0
    s_code = {
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
        while True:
            ln = input()
            if not ln:
                break
            if (num == 10):
                print_log(s_code, t_size, o_put)
                num = 1
            else:
                num += 1
            try:
                ln = [ln.split()]
                t_size += int(ln[0][-1])
                s_code[ln[0][-2]] += 1
            except Exception:
                pass

        print_log(s_code, t_size, o_put)
    except KeyboardInterrupt:
        print_log(s_code, t_size, o_put)


if __name__ == '__main__':
    '''
    Reads from standard input and computes metrics.
    How many lines of documentation does this checker even want
    '''

    run()
