"""
Given an array of size N + 1 and numbers i the range from 1 to N.
Find one duplicate. Atleast one duplicate exists
"""


def test():
    assert find_duplicate([1, 3, 2, 2]) == 2
    assert find_duplicate([1, 1, 3, 3]) in [1, 3]
    assert find_duplicate([2, 3, 3, 1]) == 3


def find_duplicate(arr):
    for i in range(len(arr)):
        if arr[i] == i + 1:
            continue
        if arr[i] == arr[arr[i] - 1]:
            return arr[i]
        temp = arr[i]
        arr[i] = arr[arr[i]]
        arr[arr[i]] = temp
