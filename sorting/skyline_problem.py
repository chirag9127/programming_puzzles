"""
Write a program to output the skyline formed by these buildings collectively
"""
import heapq
import pytest


@pytest.mark.parametrize("buildings,output", [
    ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
     [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]),
    ([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [(1, 3), (2, 0)]),
])
def test_skyline(buildings, output):
    assert skyline(buildings) == output


def skyline(buildings):
    edges = []
    for building in buildings:
        edges.append((building[0], building[2], True))
        edges.append((building[1], building[2], False))

    edges.sort(
        key=lambda x: (x[0], not x[2], -x[1])
        if x[2] is True else (x[0], not x[2], x[1]))

    heap = []
    res = []

    for edge in edges:
        if edge[2] is True:
            if len(heap) == 0 or (-1 * edge[1] < heap[0]):
                res.append((edge[0], edge[1]))
            heapq.heappush(heap, -1 * edge[1])
        else:
            heap.remove(-1 * edge[1])
            heapq.heapify(heap)
            if len(heap) == 0:
                res.append((edge[0], 0))
            elif -1 * edge[1] < heap[0]:
                res.append((edge[0], -1 * heap[0]))

    return res
