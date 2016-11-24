"""
Given an array of integers, find the sum of the elements between indices
i and j (i <= j), inclusive.
"""


class NumArray(object):

    def __init__(self, arr):
        self.sums = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.sums[i + 1] = self.sums[i] + arr[i]

    def sum_range(self, i, j):
        return self.sums[j + 1] - self.sums[i]


def test_range_sum():
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sum_range(0, 2) == 1
    assert na.sum_range(2, 5) == -1
    assert na.sum_range(0, 5) == -3
