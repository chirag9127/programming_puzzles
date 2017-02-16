"""
Given a binary tree, provide the serialization and the deserialization.
"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def test_ser_deserialize():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    assert serialize(root) == serialize(deserialize(serialize(root)))


def deserialize(ser):
    vals = iter(ser.split())
    return recursive_deser(vals)


def recursive_deser(vals):
    val = next(vals)
    if val == '#':
        return None
    node = TreeNode(int(val))
    node.left = recursive_deser(vals)
    node.right = recursive_deser(vals)
    return node


def serialize(root):
    vals = []
    preorder(root, vals)

    return ' '.join(str(v) for v in vals)


def preorder(root, vals):
    if root:
        vals.append(root.val)
        preorder(root.left, vals)
        preorder(root.right, vals)
    else:
        vals.append('#')


test_ser_deserialize()
