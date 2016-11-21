"""
Given a binary tree, provide the serialization and the deserialization.
"""
import pytest


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.__left = None
        self.__right = None

    def set_left(self, node):
        self.__left = node

    def set_right(self, node):
        self.__right = node

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right


root = TreeNode(1)
root.set_left(TreeNode(2))
root.get_left().set_right(TreeNode(3))
