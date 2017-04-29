"""
Given a list of numbers count the number of numbers smaller which are to the
right of the number.
"""
import pytest


@pytest.mark.parametrize("nums,output", [
    ([5, 2, 6, 1], [2, 1, 1, 0]),
])
def test_count_smaller(nums, output):
    assert count_smaller(nums) == output


def count_smaller(nums):
    smaller = [0] * len(nums)
    custom_sort(list(enumerate(nums)), smaller)
    return smaller


def custom_sort(enum, smaller):
    half = int(len(enum) / 2)
    if half:
        left, right = custom_sort(enum[:half], smaller), \
            custom_sort(enum[half:], smaller)
        for i in range(len(enum))[::-1]:
            if not right or left and left[-1][1] > right[-1][1]:
                print (left, right)
                smaller[left[-1][0]] += len(right)
                enum[i] = left.pop()
            else:
                enum[i] = right.pop()
    return enum


class BinaryIndexedTree(object):

    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i
