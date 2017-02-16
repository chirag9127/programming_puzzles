"""
Given N axis-aligned rectangles where N > 0, determine if they all
together form an exact cover of a rectangular region.
"""
import pytest


@pytest.mark.parametrize("rectangles,output", [
    ([
      [1, 1, 3, 3],
      [3, 1, 4, 2],
      [3, 2, 4, 4],
      [1, 3, 2, 4],
      [2, 3, 3, 4]
    ], True),
    ([
      [1, 1, 2, 3],
      [1, 3, 2, 4],
      [3, 1, 4, 2],
      [3, 2, 4, 4]
    ], False),
    ([
      [1, 1, 3, 3],
      [3, 1, 4, 2],
      [1, 3, 2, 4],
      [3, 2, 4, 4]
    ], False),
    ([
      [1, 1, 3, 3],
      [3, 1, 4, 2],
      [1, 3, 2, 4],
      [2, 2, 4, 4]
    ], False),
    ([[0, 0, 1, 1], [0, 1, 3, 2], [1, 0, 2, 2]], False),
])
def test_perfect_rectangle(rectangles, output):
    assert perfect_rectangle(rectangles) is output


def update_corners(point, corners):
    if point not in corners:
        corners[point] = 0
    corners[point] += 1


def perfect_rectangle(rectangles):
    min_point, max_point = (99999, 99999), (0, 0)
    sum_area = 0
    corners = {}
    for rec in rectangles:
        bottom_left = rec[0], rec[1]
        top_right = rec[2], rec[3]
        update_corners(bottom_left, corners)
        update_corners(top_right, corners)
        update_corners((bottom_left[0], top_right[1]), corners)
        update_corners((top_right[0], bottom_left[1]), corners)
        if bottom_left[0] <= min_point[0] and bottom_left[1] <= min_point[1]:
            min_point = bottom_left
        if top_right[0] >= max_point[0] and top_right[1] >= max_point[1]:
            max_point = top_right
        sum_area += \
            (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])
    tot_area = (max_point[0] - min_point[0]) * (max_point[1] - min_point[1])
    if tot_area != sum_area:
        return False

    edges = [min_point, max_point, (min_point[0], max_point[1]),
             (max_point[0], min_point[1])]
    for edge in edges:
        if edge not in corners or corners[edge] != 1:
            return False

    for key, val in corners.items():
        if key not in edges and val % 2 != 0:
            return False

    return True
