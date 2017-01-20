"""
Given an array of random numbers, find the kth smallest number.
E.g. in [6, 5, 8, 9, 3, 7, 4, 2] the 3rd smalles number is 4
"""
import random


def test():
    assert kth_smallest([6, 5, 8, 9, 3, 7, 4, 2], 3) == 4


def kth_smallest(array, k):
    while True:
        item = random.choice(array)
        left = []
        right = []
        for num in array:
            if num <= item:
                left.append(num)
            else:
                right.append(num)
        if len(left) == k:
            return item
        elif len(left) < k:
            # Item in right array
            array = right
            k = k - len(left)
        else:
            # Item in left array
            array = left
