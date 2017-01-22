"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and
the absolute difference between i and j is at most k.
"""
import pytest


def contains_duplicate_two_pass(nums, k):
    nums_dict = {}
    for i, num in enumerate(nums):
        if num not in nums_dict:
            nums_dict[num] = set()
        nums_dict[num].add(i)
    for i, num in enumerate(nums):
        for dup in nums_dict[num]:
            if dup == i:
                continue
            if abs(dup - i) <= k:
                return True
    return False


def contains_duplicate_one_pass(nums, k):
    nums_dict = {}
    for i, num in enumerate(nums):
        if num not in nums_dict:
            nums_dict[num] = set()
            nums_dict[num].add(i)
            continue
        else:
            for dup in nums_dict[num]:
                if abs(dup - i) <= k:
                    return True
            nums_dict[num].add(i)
    return False


@pytest.mark.parametrize("nums,k,expected_output", [
    ([2, 3, 2, 4], 2, True),
    ([1, 0, 1, 1], 1, True),
])
def test_contains_duplicate(nums, k, expected_output):
    assert contains_duplicate_two_pass(nums, k) == expected_output
    assert contains_duplicate_one_pass(nums, k) == expected_output
