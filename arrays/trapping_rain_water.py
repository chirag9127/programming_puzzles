"""
Trapping rain water
"""
import pytest


@pytest.mark.parametrize("array,output", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([2, 1, 0, 2], 3),
])
def test_trapping_water(array, output):
    assert trapping_water(array) == output


def trapping_water(array):
    left = 0
    right = len(array) - 1
    level = 0
    output = 0
    while left < right:
        if array[left] < array[right]:
            lower = array[left]
            left += 1
        else:
            lower = array[right]
            right -= 1
        level = max(level, lower)
        output += level - lower
    print (output)
    return output


trapping_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
