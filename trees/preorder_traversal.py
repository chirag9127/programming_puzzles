"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""
import pytest


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def preorder_traversal(root):
    output = []

    def traversal(root):
        # Recursive formulation of preorder traversal
        if root is None:
            return
        output.append(root.val)
        traversal(root.left)
        traversal(root.right)

    traversal(root)
    return output


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


def preorder_traversal_iterative(root):
    s = Stack()
    s.push(root)
    output = []
    while(True):
        if s.is_empty():
            break
        item = s.pop()
        if item is None:
            continue
        output.append(item.val)
        if item.right is not None:
            s.push(item.right)
        if item.left is not None:
            s.push(item.left)
    return output


def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(2)
    assert not s.is_empty()
    item = s.peek()
    assert item == 2
    item = s.pop()
    assert item == 2
    s.push(4)
    s.push(3)
    s.push(5)
    assert s.pop() == 5
    del s


@pytest.mark.parametrize("root,expected_output", [
    (TreeNode(1, right=TreeNode(2, left=TreeNode(3))), [1, 2, 3]),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), [1, 2, 3]),
    (TreeNode(1), [1]),
])
def test_preorder_traversal(root, expected_output):
    assert preorder_traversal_iterative(root) == expected_output
