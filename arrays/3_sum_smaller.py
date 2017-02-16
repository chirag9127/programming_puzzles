"""
Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.
"""
import collections
import pytest


@pytest.mark.parametrize("array,target,expected_output", [
    ([-2, 0, 1, 3], 2, 2),
])
def test_three_sum_smaller(array, target, expected_output):
    assert three_sum_smaller(array, target) == expected_output


def three_sum_smaller(array, target):
    array.sort()
    count = 0
    for k in range(len(array)):
        i, j = 0, k - 1
        while i < j:
            if array[i] + array[j] + array[k] < target:
                count += j - i
                i += 1
            else:
                j -= 1
    return count


three_sum_smaller([-2, 0, 1, 3], 2)
