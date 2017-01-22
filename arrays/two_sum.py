"""
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.
"""
import pytest


def two_sum(nums, target_sum):
    num_dict = {num: i for i, num in enumerate(nums)}
    res = []
    for i, num in enumerate(nums):
        if target_sum - num in num_dict and num_dict[target_sum - num] != i:
            res.append(i)
            res.append(num_dict[target_sum - num])
            return res


@pytest.mark.parametrize("nums,target_sum,expected_output", [
    ([2, 7, 11, 15], 9, [0, 1]),
])
def test_two_sum(nums, target_sum, expected_output):
    assert two_sum(nums, target_sum) == expected_output
