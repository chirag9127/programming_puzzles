"""
Frog jump. https://leetcode.com/problems/frog-jump/
"""
import pytest


used = {}


def frog_jump(array):
    if array[1] > 1:
        return False
    for i in range(len(array)):
        used[i] = {}
    return count(array, 1, 1)


def count(array, pos, steps):
    if steps in used[pos]:
        return used[pos][steps]
    if len(array) - pos == 1:
        return True
    for i in range(pos + 1, len(array)):
        if array[i] - array[pos] > steps + 1:
            break
        if steps - 1 <= array[i] - array[pos] <= steps + 1:
            if count(array, i, array[i] - array[pos]):
                used[i][array[i] - array[pos]] = True
                return True
            else:
                used[i][array[i] - array[pos]] = False
    return False


@pytest.mark.parametrize("input_array,expected_output", [
    ([0, 2], False),
    ([0, 1, 3, 5, 6, 8, 12, 17], True),
    ([0, 1, 2, 3, 4, 8, 9, 11], False),
])
def test_frog_jump(input_array, expected_output):
    assert frog_jump(input_array) == expected_output
