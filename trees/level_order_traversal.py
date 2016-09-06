"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""
import pytest


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def end(self):
        return self.items[-1]


def level_order_traversal(root):
    if root is None:
        return []
    q = Queue()
    q.enqueue(root)
    q.enqueue(None)
    output = []
    curr = []
    while not q.is_empty():
        item = q.dequeue()
        if item is None:
            if not q.is_empty():
                q.enqueue(None)
            output.append(curr)
            curr = []
            continue
        if item.left is not None:
            q.enqueue(item.left)
        if item.right is not None:
            q.enqueue(item.right)
        curr.append(item.val)
    return output


@pytest.mark.parametrize("root,expected_output", [
    (TreeNode(1), [[1]]),
    (None, []),
    (TreeNode(3, left=TreeNode(9),
              right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))),
     [[3], [9, 20], [15, 7]]),
])
def test_level_order_traversal(root, expected_output):
    assert level_order_traversal(root) == expected_output
