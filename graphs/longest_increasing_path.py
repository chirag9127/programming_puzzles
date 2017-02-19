"""
Given an integer matrix, find the length of the longest increasing path.
"""
import pytest


@pytest.mark.parametrize("matrix,length", [
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
])
def test_longest_increasing_path(matrix, length):
    assert longest_increasing_path(matrix) == length


def longest_increasing_path(matrix):
    max_length = 0
    memo = [[0 for j in range(len(matrix[0]))]
            for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_length = max(max_length, dfs(i, j, matrix, memo))

    return max_length


def dfs(x, y, matrix, memo):
    if not memo[x][y]:
        memo[x][y] = 1 + \
            max(dfs(k, l, matrix, memo) if 0 <= k < len(matrix) and
                0 <= l < len(matrix[0]) and matrix[k][l] > matrix[x][y] else 0
                for k, l in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)])

    return memo[x][y]
