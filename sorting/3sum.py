"""
Given an array S of n integers, are there elements a, b, c in S such
that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.
https://leetcode.com/problems/3sum/
"""
import pytest


def is_odd(num):
    if num % 2 == 0:
        return False
    return True


def find_3sums(arr):
    """
    O(n^2) algorithm to reduce the search space to find the 3 sum
    """
    output = []
    count = 0
    sorted_array = sorted(arr)
    i = 0
    j = len(sorted_array) - 1
    k = i + 1
    while(True):
        found = False
        if i == j - 1:
            break
        for k in range(i + 1,  j):
            if arr[i] + arr[j] + arr[k] == 0:
                output.append([arr[i], arr[j], arr[k]])
                break
        if found is True:
            continue
        elif is_odd(count):
            i += 1
        else:
            j -= 1
        count += 1
    return output


def find_3sums_alternate(arr):
    """
    O(n^2) algorithm to reduce the search space to find the 3 sum. This does
    it more efficiently than the above algorithm.
    """
    output = []
    arr = sorted(arr)
    for i in range(len(arr) - 2):
        if arr[i] == arr[i - 1]:
            continue
        start, end = i + 1, len(arr) - 1
        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                output.append([arr[i], arr[start], arr[end]])
                start += 1
                end -= 1
                while start < end and arr[start] == arr[start - 1]:
                    start += 1
                while end > start and arr[end] == arr[end + 1]:
                    end -= 1
            elif arr[start] + arr[end] > -(arr[i]):
                end -= 1
            else:
                start += 1
    return output


@pytest.mark.parametrize("input_array,expected_output", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
])
def test_3sum(input_array, expected_output):
    assert find_3sums_alternate(input_array) == expected_output
