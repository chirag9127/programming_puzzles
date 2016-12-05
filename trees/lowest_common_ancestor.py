"""
Given a binary tree and two nodes, find the lowest common ancestor of the
two nodes.
"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def test_lca():
    root = TreeNode(3)
    root_left = TreeNode(5)
    root_right = TreeNode(1)
    root.left = root_left
    root.right = root_right
    root_left_left = TreeNode(6)
    root_left_right = TreeNode(2)
    root_left.left = root_left_left
    root_left.right = root_left_right
    root_left_right_left = TreeNode(7)
    root_left_right_right = TreeNode(4)
    root_left_right.left = root_left_right_left
    root_left_right.right = root_left_right_right
    root_right_left = TreeNode(0)
    root_right.left = root_right_left
    root_right_right = TreeNode(8)
    root_right.right = root_right_right
    assert lca(root, root_left, root_right) == root
    assert lca(root, root_left, root_left_right_right) == root_left


def lca(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    if left and right:
        return root
    return left if left else right
