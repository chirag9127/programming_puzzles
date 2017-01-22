"""
Given an array of integers, every element appears twice except for one.
Find that single one.
"""
import pytest


@pytest.mark.parametrize("nums,expected_output", [
    ([2, 1, 2], 1),
    ([3, 3, 5, 2, 5], 2),
])
def test_single_number(nums, expected_output):
    assert single_number(nums) == expected_output


def single_number(nums):
    out = 0
    for num in nums:
        out ^= num
    return out
