"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert(array):
    if len(array) == 0:
        return None
    mid_index = (len(array) - 1) / 2
    left = array[:mid_index]
    right = array[mid_index + 1:]
    node = TreeNode(array[mid_index])
    node.left = convert(left)
    node.right = convert(right)
    return node


def test_convert():
    array = [0, 1, 2]
    root = convert(array)
    assert root.val == 1
    assert root.left.val == 0
    assert root.right.val == 2
