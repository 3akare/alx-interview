#!/usr/bin/python3
'''
Rotate a 2D matrix
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate a 2d Matrix
    '''
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    # Reverse each list in the matrix
    for ma in matrix:
        ma.reverse()
