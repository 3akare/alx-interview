#!/usr/bin/python3
"""
n-Queens - Backtracking
"""

from sys import argv, exit as sexit
# Compared to the exit() builtin function, sys.exit() is more concise.
# So I imported it as sexit... ;p


def verify_argv():
    """
    Verifies the value gotten from sys.argv[0]
    """
    try:
        if len(argv) > 2:
            raise IndexError
        try:
            number = int(argv[1])
        except ValueError:
            print('N must be a number')
            sexit(1)
        if number < 4:
            print('N must be at least 4')
            sexit(1)
    except IndexError:
        print('Usage: nqueens N')
        sexit(1)
    return number


def solve_n_queens(n):
    """
    This function takes an integer `n` as input and returns a list of lists,
    """
    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_helper(n, 0, board, solutions)
    return solutions


def solve_n_queens_helper(n, row, board, solutions):
    """
    This is a recursive function that takes four arguments: `n`
    (the size of the board),
    """
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, row, i):
            board[row][i] = 1
            solve_n_queens_helper(n, row+1, board, solutions)
            board[row][i] = 0


def is_safe(board, row, col):
    """
    is_safe - This function takes three arguments: `row` (the
    current row being considered)
    """
    n = len(board)

    # Check row and column
    for i in range(n):
        if board[i][col] == 1 or board[row][i] == 1:
            return False

    # Check diagonals
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def print_solutions(n):
    """
    Prints out the solutions
    """
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


def run():
    """
    Solve and print out the solutions
    """
    n = verify_argv()
    print_solutions(n)


if __name__ == '__main__':
    run()
