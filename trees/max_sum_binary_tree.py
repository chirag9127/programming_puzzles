"""
Given a binary tree, find the maximum path sum.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_path_sum(root):
    # A leaf None node is 0
    if not root:
        return 0
    # We can go down the left and right subtrees. If either of them return
    # a negative result then it cannot be considered in the maximum path.
    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)
    max_single = max(max(left_sum, right_sum) + root.val, root.val)
    max_root = max(max_single, left_sum + right_sum + root.val)
    max_path_sum.res = max(max_root, max_path_sum.res)
    return max_single


def max_path_init(root):
    max_path_sum.res = - 999999
    max_path_sum(root)
    return max_path_sum.res


def test_max_path_sum():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert max_path_init(root) == 6

    root = TreeNode(-2)
    root.left = TreeNode(1)
    assert max_path_init(root) == 1

    root = TreeNode(-3)
    assert max_path_init(root) == -3

    root = TreeNode(1)
    root.right = TreeNode(-2)
    assert max_path_init(root) == 1

    root = TreeNode(-2)
    root.right = TreeNode(-1)
    assert max_path_init(root) == -1
