"""
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.
"""
import pytest


@pytest.mark.parametrize("matrix,expected_output", [
    ([['1', '0', '1', '0', '0'],
      ['1', '0', '1', '1', '1'],
      ['1', '1', '1', '1', '1'],
      ['1', '0', '0', '1', '0']], 4),
])
def test_maximal_square(matrix, expected_output):
    assert maximal_square(matrix) == expected_output


def all_ones(square):
    for i in range(len(square)):
        for j in range(len(square[0])):
            if square[i][j] == '0':
                return False
    return True


def maximal_square(matrix):
    """
    For each point in the matrix try increasingly bigger
    right diagonal squares stopping when one of the squares contains a zero or
    the square's dimensions don't fit in the matrix
    """
    size = 0
    range_matrix = [[0 for j in range(len(matrix[0]))]
                    for i in range(len(matrix))]
    range_matrix[0][0] = int(matrix[0][0])
    for i in xrange(1, len(matrix)):
        range_matrix[i][0] = range_matrix[i - 1][0] + int(matrix[i][0])
    for j in xrange(1, len(matrix[0])):
        range_matrix[0][j] = range_matrix[0][j - 1] + int(matrix[0][j])
    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix[0])):
            range_matrix[i][j] = range_matrix[i - 1][j] + \
                range_matrix[i][j - 1] - range_matrix[i - 1][j - 1] + \
                int(matrix[i][j])
    square_size = 2
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                continue
            if size == 0:
                size = 1
            square_sum = 0
            while i + square_size < len(range_matrix) and \
                    j + square_size < len(range_matrix[0]):
                if i == 0 and j == 0:
                    square_sum = \
                        range_matrix[i + square_size - 1][j + square_size - 1]
                elif i == 0:
                    square_sum = \
                        range_matrix[i + square_size - 1][j + square_size - 1] \
                        - range_matrix[i + square_size - 1][j - 1]
                elif j == 0:
                    square_sum = \
                        range_matrix[i + square_size - 1][j + square_size - 1] \
                        - range_matrix[i - 1][j + square_size - 1]
                else:
                    square_sum = \
                        range_matrix[i + square_size - 1][j + square_size - 1] \
                        - range_matrix[i - 1][j + square_size - 1] \
                        - range_matrix[i + square_size - 1][j - 1] \
                        + range_matrix[i - 1][j - 1]
                if square_sum == square_size ** 2:
                    size = square_size ** 2
                    square_size += 1
                else:
                    break
    return size


def maximal_square_2(A):
    area = 0
    if A:
        p = [0] * len(A[0])
        for row in A:
            print p
            s = map(int, row)
            for j, c in enumerate(s[1:], 1):
                s[j] *= min(p[j-1], p[j], s[j-1]) + 1
            print s
            area = max(area, max(s) ** 2)
            p = s
    return area
