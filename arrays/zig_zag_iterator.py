"""
Given two 1d vectors, implement an iterator to return
their elements alternately.
"""


class ZigzagIterator(object):

    def __init__(self, matrix):
        self.data = [(len(v), iter(v)) for v in matrix if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len - 1, iter))
        return next(iter)

    def has_next(self):
        return bool(self.data)


def test_zig_zag_iterator():
    res = []
    i = ZigzagIterator([[1, 2], [3, 4, 5, 6]])
    while i.has_next():
        n = i.next()
        res.append(n)
    assert res == [1, 3, 2, 4, 5, 6]

    res = []
    i = ZigzagIterator([[1, 2, 3], [4, 5, 6, 7], [8, 9]])
    while i.has_next():
        n = i.next()
        res.append(n)
    assert res == [1, 4, 8, 2, 5, 9, 3, 6, 7]


test_zig_zag_iterator()
