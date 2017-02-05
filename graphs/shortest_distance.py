"""
You want to build a house on an empty land which reaches all buildings
in the shortest amount of distance.
You can only move up, down, left and right.
"""
import collections
import pytest


@pytest.mark.parametrize("grid,expected_output", [
    ([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7),
    ([[1, 2, 0]], -1),
    ([[1, 1], [0, 1]], -1),
])
def test_shortest_distance(grid, expected_output):
    assert shortest_distance(grid) == expected_output


def shortest_distance(grid):
    distances = [[0] * len(grid[0]) for i in range(len(grid))]
    hits = [[0] * len(grid[0]) for i in range(len(grid))]
    num_buildings = sum(grid[i][j] for j in range(len(grid[0]))
                        for i in range(len(grid)) if grid[i][j] == 1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count_buildings = bfs(i, j, grid, distances, hits)
                if count_buildings < num_buildings:
                    return -1
    min_distance = min([distances[i][j] for j in range(len(grid[0]))
                        for i in range(len(grid)) if grid[i][j] == 0 and
                        hits[i][j] == num_buildings] or [-1])
    if min_distance == 0:
        return -1
    return min_distance


def bfs(x, y, grid, distances, hits):
    visited = [[False] * len(grid[0]) for i in range(len(grid))]
    queue = collections.deque()
    for k, p in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= k < len(grid) and 0 <= p < len(grid[0]):
            queue.append((k, p, 1))
    visited[x][y] = True
    count_buildings = 1
    while len(queue) > 0:
        curr_x, curr_y, curr_dist = queue.popleft()
        if visited[curr_x][curr_y]:
            continue
        visited[curr_x][curr_y] = True
        if grid[curr_x][curr_y] == 1:
            count_buildings += 1
        elif grid[curr_x][curr_y] == 0:
            distances[curr_x][curr_y] += curr_dist
            hits[curr_x][curr_y] += 1
            for k, p in ((curr_x + 1, curr_y), (curr_x - 1, curr_y),
                         (curr_x, curr_y - 1), (curr_x, curr_y + 1)):
                if 0 <= k < len(grid) and 0 <= p < len(grid[0]) and \
                        visited[k][p] is False:
                    queue.append((k, p, curr_dist + 1))
    return count_buildings
