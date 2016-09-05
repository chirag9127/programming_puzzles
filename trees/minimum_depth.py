"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.
"""
import pytest


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def minimum_depth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minimum_depth(root.right) + 1
    if root.right is None:
        return minimum_depth(root.left) + 1
    return min(minimum_depth(root.left), minimum_depth(root.right)) + 1


@pytest.mark.parametrize("root,expected_output", [
    (None, 0),
    (TreeNode(1, right=TreeNode(2)), 2),
    (TreeNode(1), 1),
    (TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4)), 2),
])
def test_minimum_depth(root, expected_output):
    assert minimum_depth(root) == expected_output
