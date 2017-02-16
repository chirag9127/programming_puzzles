"""
Given a list of positions to operate,
count the number of islands after each addLand operation.
"""
import pytest


@pytest.mark.parametrize("m,n,positions,expected_output", [
    (3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]], [1, 1, 2, 3]),
    (3, 3, [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]], [1, 1, 2, 3, 1]),
    (3, 3, [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]],
     [1, 2, 3, 4, 3, 2, 1]),
])
def test_num_islands(m, n, positions, expected_output):
    assert num_islands(m, n, positions) == expected_output


def num_islands(m, n, positions):
    if len(positions) == 0:
        return 0
    parents = {}
    counts = [1]

    parents[tuple(positions[0])] = -1

    count = 1

    for i in range(1, len(positions)):
        curr_x, curr_y = positions[i][0], positions[i][1]
        parents[(curr_x, curr_y)] = -1
        count += 1
        for new_x, new_y in (curr_x + 1, curr_y), (curr_x - 1, curr_y), \
                (curr_x, curr_y + 1), (curr_x, curr_y - 1):
            num = visit_and_mark(
                curr_x, curr_y, new_x, new_y, parents, m, n)
            count -= num
        counts.append(count)

    return counts


def visit_and_mark(curr_x, curr_y, x, y, parents, m, n):
    if (x >= m or x < 0) or (y >= n or y < 0):
        return 0

    if (x, y) not in parents:
        return 0

    temp_x, temp_y = x, y
    while parents[(temp_x, temp_y)] != -1 and \
            (temp_x, temp_y) != parents[(temp_x, temp_y)]:
        temp_x, temp_y = parents[(temp_x, temp_y)]

    if (temp_x, temp_y) != (curr_x, curr_y):
        parents[(temp_x, temp_y)] = (curr_x, curr_y)
        return 1
    return 0
