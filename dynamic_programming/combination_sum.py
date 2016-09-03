"""
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up
to a positive integer target.
https://leetcode.com/problems/combination-sum-iv/
"""
import pytest


def combination_sum(input_array, target):
    outputs = [0] * (target + 1)
    for i in range(1, target + 1):
        for j in range(len(input_array)):
            if i - input_array[j] == 0:
                outputs[i] += 1
            elif i - input_array[j] > 0:
                outputs[i] += outputs[i - input_array[j]]
    return outputs[-1]


@pytest.mark.parametrize("input_array,target,expected_output", [
    ([2, 3, 5], 10, 14),
    ([1, 2, 3], 4, 7),
])
def test_combination_sum(input_array, target, expected_output):
    assert combination_sum(input_array, target) == expected_output
