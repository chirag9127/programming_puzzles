"""
Given an m x n matrix of positive integers representing the height of each unit
cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.
"""
import pytest
import heapq


@pytest.mark.parametrize("matrix,output", [
    ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
])
def test_trapping_rain_water(matrix, output):
    assert trapping_rain_water(matrix) == output


def trapping_rain_water(matrix):
    heap = []
    visited = [[False for j in range(len(matrix[0]))]
               for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0 or i == len(matrix) - 1 or \
                    j == len(matrix[0]) - 1:
                heapq.heappush(heap, (matrix[i][j], i, j))
                visited[i][j] = True

    result = 0
    while len(heap) > 0:
        height, x, y = heapq.heappop(heap)
        for i, j in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) - 1 and \
                    not visited[i][j]:
                result += max(0, height - matrix[i][j])
                heapq.heappush(heap, (max(height, matrix[i][j]), i, j))
                visited[i][j] = True

    return result


trapping_rain_water([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4],
                     [2, 3, 3, 2, 3, 1]])
