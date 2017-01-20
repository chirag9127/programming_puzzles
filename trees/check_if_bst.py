"""
Given a binary tree check if the tree is a binary search tree or not
"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def test():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    assert check_if_bst(root) == True

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    assert check_if_bst(root) == False


def check_if_bst(root, min_possible=-9999, max_possible=9999):
    if root is None:
        return True
    if min_possible <= root.val <= max_possible:
        left = check_if_bst(root.left, min_possible, root.val)
        right = check_if_bst(root.right, root.val, max_possible)
        if left and right:
            return True
        return False
    return False
