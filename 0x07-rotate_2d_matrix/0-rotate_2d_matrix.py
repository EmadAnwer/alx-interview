#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix: list):
    """Rotate a 2D matrix by 90 degrees"""
    length = len(matrix[0])
    matrix.extend([[] for _ in range(length)])

    for i in range(len(matrix), len(matrix) - length, -1):
        for j in range(len(matrix) - length, 0, -1):
            matrix[i - 1].append(matrix[j - 1].pop())
    del matrix[0 : len(matrix) - length]


# Pythonic way
# def rotate_2d_matrix(matrix: list):
#     matrix[:] = [list(row) for row in zip(*matrix[::-1])]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# optimized way
# def rotate_2d_matrix(matrix: list):
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range(i, n - i - 1):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[n - 1 - j][i]
#             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
#             matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
#             matrix[j][n - 1 - i] = temp
