"""
You are given an m * n matrix. Return the total number of paths
"""
import pytest


@pytest.mark.parametrize("a,expected_output", [
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 10),
    ([[1, 1], [0, 1]], 1),
])
def test_num_of_paths(a, expected_output):
    assert num_of_paths(a) == expected_output


def num_of_paths(a):
    copy = [[0 for j in range(len(a[0]))] for i in range(len(a))]

    default = 1
    for i in range(len(a)):
        if a[i][0] == 0:
            default = 0
        copy[i][0] = default

    default = 1
    for i in range(len(a[0])):
        if a[0][i] == 0:
            default = 0
        copy[0][i] = default

    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            curr = 0
            if a[i - 1][j] == 1:
                curr += copy[i - 1][j]
            if a[i][j - 1] == 1:
                curr += copy[i][j - 1]
            if a[i][j] == 0:
                curr = 0
            copy[i][j] = curr
