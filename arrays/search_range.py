"""
Given a sorted array of integers, find the starting and ending position
of a given target value.
"""
import pytest


def search_range(input_arr, target):
    low = 0
    high = len(input_arr) - 1
    found = False
    while low <= high:
        mid = (low + high) / 2
        print mid, low, high
        if input_arr[mid] == target:
            found = True
            break
        elif input_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if not found:
        return [-1, -1]
    if found and input_arr[mid - 1] != target and input_arr[mid + 1] != target:
        return [mid, mid]
    left_low = 0
    left_high = mid
    while left_low <= left_high:
        left_mid = (left_low + left_high) / 2
        print left_mid, left_low, left_high
        if input_arr[left_mid] == target and input_arr[left_mid - 1] != target:
            break
        elif input_arr[left_mid] == target and \
                input_arr[left_mid - 1] == target:
            left_high = left_mid
        else:
            left_low = left_mid + 1
    right_low = mid
    right_high = len(input_arr) - 1
    while right_low < right_high:
        right_mid = (right_low + right_high) / 2
        if input_arr[right_mid] == target and \
                input_arr[right_mid + 1] != target:
            break
        elif input_arr[right_mid] == target and \
                input_arr[right_mid + 1] == target:
            right_low = right_mid
        else:
            right_high = right_mid - 1
    return [left_mid, right_mid]


@pytest.mark.parametrize("input_arr,target,expected_output", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 11, [-1, -1]),
])
def test_search_range(input_arr, target, expected_output):
    assert search_range(input_arr, target) == expected_output
