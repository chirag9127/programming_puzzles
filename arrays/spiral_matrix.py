"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.
"""
import pytest


def spiral_matrix(matrix):
    output = []
    while(len(matrix) > 0 and len(matrix[0]) > 0):
        # Go horizontal right
        for i in range(len(matrix[0])):
            output.append(matrix[0][i])
        if len(matrix) == 1:
            # special case when there is only one row
            break
        # Go vertically down
        for i in range(1, len(matrix)):
            output.append(matrix[i][len(matrix[0]) - 1])
        # Go horizontally left
        for i in range(len(matrix[0]) - 2, -1, -1):
            output.append(matrix[len(matrix) - 1][i])
        # Go vertically up
        if len(matrix[0]) == 1:
            # special case when there is only one column
            break
        for i in range(len(matrix) - 2, 0, -1):
            output.append(matrix[i][0])
        matrix = [[matrix[i][j] for j in range(1, len(matrix[0]) - 1)]
                  for i in range(1, len(matrix) - 1)]
    return output


@pytest.mark.parametrize("matrix,expected_output", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1]], [1]),
    ([[2, 3]], [2, 3])
])
def test_spiral_matrix(matrix, expected_output):
    assert spiral_matrix(matrix) == expected_output


print spiral_matrix([[7], [9], [6]])
