#!/usr/bin/python3
""" Rotate 2D Matrix """
def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix,
      rotate it 90 degrees clockwise """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
