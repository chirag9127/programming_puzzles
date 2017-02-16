"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
"""
import collections
import pytest


@pytest.mark.parametrize("maze,expected_output", [
    ([[1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]], 1),
    ([[1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1]], 3),
])
def test_count_islands(maze, expected_output):
    assert count_islands(maze) == expected_output


def count_islands(maze):
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                visit_and_mark(i, j, maze)
                count += 1
                print(maze)
    return count


def visit_and_mark(i, j, maze):
    queue = collections.deque()
    queue.append((i, j))

    while len(queue) > 0:
        x, y = queue.popleft()
        maze[x][y] = -1
        for k, l in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= k < len(maze) and 0 <= l < len(maze[0]) and \
                    maze[k][l] == 1:
                queue.append((k, l))
