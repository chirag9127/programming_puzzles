"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""
import pytest


def find_median(nums1, nums2):
    if len(nums1) < len(nums2):
        find_median_utils(nums1, nums2)
    find_median_utils(nums2, nums1)


def find_median_one_array(nums):
    if len(nums) % 2 == 0:
        return (nums[(len(nums) - 1)/2] + nums[((len(nums) - 1)/2) + 1]) / 2.0
    return nums[len(nums)/2]


def find_median_utils(nums1, nums2):
    if len(nums1) == 0:
        find_median_one_array(nums2)

"""
@pytest.mark.paramatrize("nums1,nums2,expected_output", [
    ([1], [2, 3, 4, 5, 6], 3.5),
    ([1, 2, 3], [4, 5, 6], 3.5),
    ([1, 3], [2], 2.5),
    ([1, 3, 5], [2, 3, 4], 3),
])
def test_find_medians(nums1, nums2, expected_output):
    assert find_median(nums1, nums2) == expected_output
"""


@pytest.mark.parametrize("nums,expected_output", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4], 2.5),
])
def test_find_median_one_array(nums, expected_output):
    find_median_one_array(nums) == expected_output
