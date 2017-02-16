"""
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.
"""
import collections
import pytest


@pytest.mark.parametrize("matrix,output", [
    ([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
      [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]],
     [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
])
def test_walls_and_gates(matrix, output):
    assert walls_and_gates(matrix) == output


def walls_and_gates(matrix):
    queue = collections.deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                queue.append((i, j, 0))

    bfs(queue, matrix)
    print(matrix)


def bfs(queue, matrix):
    visited = [[False for j in range(len(matrix[0]))]
               for i in range(len(matrix))]

    while len(queue) > 0:
        curr_x, curr_y, count = queue.popleft()
        visited[curr_x][curr_y] = True
        matrix[curr_x][curr_y] = min(matrix[curr_x][curr_y], count)

        for i, j in (curr_x, curr_y + 1), (curr_x, curr_y - 1), \
                (curr_x + 1, curr_y), (curr_x - 1, curr_y):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and \
                    not visited[i][j] and matrix[i][j] != -1:
                queue.append((i, j, count + 1))
