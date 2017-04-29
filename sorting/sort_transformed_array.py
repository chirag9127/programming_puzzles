"""
Given a sorted array of integers nums and integer values a, b and c.
"""
import pytest


@pytest.mark.parametrize("nums,a,b,c,output", [
    ([-4, -2, 2, 4], 1, 3, 5, [3, 9, 15, 33]),
    ([-4, -2, 2, 4], -1, 3, 5, [-23, -5, 1, 7]),
])
def test_sort_transformed_array(nums, a, b, c, output):
    assert sort_transformed_array(nums, a, b, c) == output


def sort_transformed_array(nums, a, b, c):
    result = [0] * len(nums)
    start = 0
    end = len(nums) - 1
    curr = 0 if a < 0 else len(nums) - 1
    while start <= end:
        start_num = transformation(nums[start], a, b, c)
        end_num = transformation(nums[end], a, b, c)
        if a >= 0:
            if start_num >= end_num:
                result[curr] = start_num
                curr -= 1
                start += 1
            else:
                result[curr] = end_num
                curr -= 1
                end -= 1
        else:
            if start_num <= end_num:
                result[curr] = start_num
                curr += 1
                start += 1
            else:
                result[curr] = end_num
                curr += 1
                end -= 1
    return result


def transformation(x, a, b, c):
    return a * x * x + b * x + c
