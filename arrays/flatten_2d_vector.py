"""
Implement an iterator to flatten a 2d vector.
"""


class Vector2D(object):

    def __init__(self, vec2d):
        self.x = 0
        self.y = 0
        self.vec = vec2d

    def next(self):
        result = self.vec[self.x][self.y]
        self.y += 1
        return result

    def has_next(self):
        while self.x < len(self.vec):
            if self.y < len(self.vec[self.x]):
                return True
            self.y = 0
            self.x += 1
        return False


def test():
    vec2d = [[1, 2], [3], [4, 5, 6]]
    i, v = Vector2D(vec2d), []
    while i.has_next():
        v.append(i.next())
    assert v == [1, 2, 3, 4, 5, 6]
