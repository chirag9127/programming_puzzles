"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken
into on the same night.
"""
import pytest


def house_robber(nums):
    max_amt = [0] * len(nums)
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    max_amt[0], max_amt[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        max_amt[i] = max(max_amt[i - 1], max_amt[i - 2] + nums[i])
    return max_amt[-1]


@pytest.mark.parametrize("nums,expected_output", [
    ([2, 3, 4], 6),
    ([], 0),
    ([1], 1),
    ([2, 7, 3], 7)
])
def test_house_robber(nums, expected_output):
    assert house_robber(nums) == expected_output
