"""
Search in a rotated sorted array.
"""
import pytest


def find_changing_element(nums):
    if nums[0] < nums[len(nums) - 1]:
        return -1
    left = 0
    right = len(nums) - 1
    mid = (left + right) / 2
    while nums[mid - 1] < nums[mid] < nums[mid + 1]:
        if nums[mid] > nums[left]:
            left = mid
        else:
            right = mid
        mid = (left + right) / 2
    if nums[mid - 1] > nums[mid] < nums[mid + 1]:
        return mid - 1
    return mid


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        print left, right, mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search(nums, target):
    index = find_changing_element(nums)
    if index < 0:
        bs = binary_search(nums, target)
        if bs >= 0:
            return bs
        return -1
    left_arr, right_arr = nums[:index + 1], nums[index + 1:]
    lbs = binary_search(left_arr, target)
    rbs = binary_search(right_arr, target)
    if lbs >= 0:
        return lbs
    elif rbs >= 0:
        return rbs + len(left_arr)
    return -1


@pytest.mark.parametrize("nums,target,expected_output", [
    ([4, 5, 6, 7, 0, 1, 2], 5, 1),
    ([4, 5, 6, 7, 8, 9, 0, 1, 2], 1, 7),
    ([1, 3, 5], 0, -1)
])
def test_search(nums, target, expected_output):
    assert search(nums, target) == expected_output
