"""
Shortest path from start to destination in a maze.
"""
import heapq
import pytest


@pytest.mark.parametrize("maze,start,destination,expected_output", [
    ([[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]], (0, 4), (4, 4), 12),

    ([[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]], (0, 4), (3, 2), -1),

    ([[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]], (0, 4), (1, 2), 9),

    ([[0, 0, 1, 0, 0]], (0, 1), (0, 3), -1),
])
def test_maze(maze, start, destination, expected_output):
    assert find(maze, start, destination) == expected_output


def find(maze, start, destination):
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()
    distances = {}

    while len(heap) > 0:
        min_item = heapq.heappop(heap)
        dist, location = min_item[0], min_item[1]
        distances[location] = dist
        if location == destination:
            break
        visited.add(location)
        temp_x, temp_y = location[0], location[1]
        i = 1
        while temp_x + i < len(maze) and maze[temp_x + i][temp_y] == 0:
            i += 1
        new_dist = i - 1
        if new_dist != 0 and (temp_x + new_dist, temp_y) not in visited:
            heapq.heappush(heap, (dist + new_dist, (temp_x + new_dist, temp_y)))

        i = 1
        while temp_x - i >= 0 and maze[temp_x - i][temp_y] == 0:
            i += 1
        new_dist = i - 1
        if new_dist != 0 and (temp_x - new_dist, temp_y) not in visited:
            heapq.heappush(heap, (dist + new_dist, (temp_x - new_dist, temp_y)))

        i = 1
        while temp_y + i < len(maze[0]) and maze[temp_x][temp_y + i] == 0:
            i += 1
        new_dist = i - 1
        if new_dist != 0 and (temp_x, temp_y + new_dist) not in visited:
            heapq.heappush(heap, (dist + new_dist, (temp_x, temp_y + new_dist)))

        i = 1
        while temp_y - i >= 0 and maze[temp_x][temp_y - i] == 0:
            i += 1
        new_dist = i - 1
        if new_dist != 0 and (temp_x, temp_y - new_dist) not in visited:
            heapq.heappush(heap, (dist + new_dist, (temp_x, temp_y - new_dist)))
    if destination in distances:
        return distances[destination]
    return -1
