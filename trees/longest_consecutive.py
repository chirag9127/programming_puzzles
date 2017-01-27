"""
Given a binary tree, find the length of the longest consecutive sequence path.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test_longest_consecutive():
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    assert longest_consecutive(root) == 3

    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(1)
    assert longest_consecutive(root) == 2


def longest_consecutive(root):

    def get_longest_consecutive(root, output):
        if root is None:
            return 0
        if not root.left and not root.right:
            if output['longest_length'] == 0:
                output['longest_length'] = 1
                output['longest_node'] = root.val
            return 1
        left_len = get_longest_consecutive(root.left, output)
        right_len = get_longest_consecutive(root.right, output)
        root_in_left_path = False
        root_in_right_path = False
        if root.left and root.val == root.left.val - 1:
            # root involved in the left path
            root_in_left_path = True
            left_len += 1
            if left_len > output['longest_length']:
                output['longest_length'] = left_len
                output['longest_node'] = root.val
        if root.right and root.val == root.right.val - 1:
            root_in_right_path = True
            right_len += 1
            if right_len > output['longest_length']:
                output['longest_length'] = right_len
                output['longest_node'] = root.val
        if right_len >= left_len and root_in_right_path:
            return right_len
        if left_len >= right_len and root_in_left_path:
            return left_len
        return 1

    output = {'longest_length': 0, 'longest_node': None}
    get_longest_consecutive(root, output)
    return output['longest_length']
