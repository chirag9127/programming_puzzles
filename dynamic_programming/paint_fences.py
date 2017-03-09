"""
There is a fence with n posts, each post can be painted with
one of the k colors.
"""


def paint_fences(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same, diff = k, k * (k - 1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff
