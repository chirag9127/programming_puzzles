"""
Find the list of grid coordinates where water can flow to both the
Pacific and Atlantic ocean.
"""
import pytest


@pytest.mark.parametrize("matrix,expected_output", [
    ([[1, 2, 2, 3, 5],
      [3, 2, 3, 4, 4],
      [2, 4, 5, 3, 1],
      [6, 7, 1, 4, 5],
      [5, 1, 1, 2, 4]],
     [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]),
])
def test_water_flow(matrix, expected_output):
    assert set(water_flow(matrix)) == set(expected_output)


def water_flow(matrix):
    output = []
    atlantic = [[False for j in range(len(matrix[0]))]
                for i in range(len(matrix))]
    pacific = [[False for j in range(len(matrix[0]))]
               for i in range(len(matrix))]

    for i in range(len(matrix)):
        check(i, 0, matrix, pacific)
        check(i, len(matrix[0]) - 1, matrix, atlantic)

    for j in range(len(matrix[0])):
        check(0, j, matrix, pacific)
        check(len(matrix) - 1, j, matrix, atlantic)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if pacific[i][j] and atlantic[i][j]:
                output.append((i, j))
    return output


def check(i, j, matrix, visited):
    visited[i][j] = True

    for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                matrix[x][y] >= matrix[i][j] and \
                not visited[x][y]:
            check(x, y, matrix, visited)
