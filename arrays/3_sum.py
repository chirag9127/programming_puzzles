"""
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""
import pytest


@pytest.mark.parametrize("array,expected_output", [
    ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
])
def test_3sum(array, expected_output):
    assert three_sum(array) == expected_output


def three_sum(array):
    array.sort()
    output = set()
    for i in range(len(array) - 2):
        start = i + 1
        end = len(array) - 1
        while start < end:
            if array[i] + array[start] + array[end] == 0:
                output.add((array[i], array[start], array[end]))
                end -= 1
            elif array[i] + array[start] + array[end] > 0:
                end -= 1
            else:
                start += 1
    output = list(output)
    return output
