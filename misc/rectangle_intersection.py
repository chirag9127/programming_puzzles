"""
Given a list of rectangles defined by their diagonals, give the number of
rectangles which intersect.
"""


class Rectangle(object):

    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.bottom_left = (self.top_left[0], self.bottom_right[1])
        self.top_right = (self.bottom_right[0], self.top_left[1])

    def points(self):
        return [self.top_left, self.bottom_left, self.top_right,
                self.bottom_right]


def test_rectangle_intersection():
    r1 = Rectangle((3, 4), (5, 2))
    r2 = Rectangle((4, 3), (7, 1))
    r3 = Rectangle((5, 6), (8, 5))

    assert rectangle_intersection([r1, r2, r3]) == 1


def rectangle_intersection(rectangles):
    count_intersection = 0
    for i in range(len(rectangles) - 1):
        for j in range(1, len(rectangles)):
            if i == j:
                continue
            if pair_intersection(rectangles[i], rectangles[j]):
                count_intersection += 1
    return count_intersection


def pair_intersection(rect1, rect2):
    # Case 1: rect1 subsumes rect2 or vice versa
    if subsumes(rect1, rect2) or subsumes(rect2, rect1):
        return True

    # Case 2: one point is the same
    if point_intersection(rect1, rect2):
        return True

    # Case 3: one corner intersects
    if one_corner_intersect(rect1, rect2) or \
            one_corner_intersect(rect2, rect1):
        return True

    """
    if one_side_intersect(rect1, rect2) or \
            one_side_intersect(rect2, rect2):
        return True
    """
    return False


def one_side_intersect(rect1, rect2):
    if rect2.top_left[0] <= rect1.top_right[0] <= rect2.top_right[0] and \
            rect2.bottom_left[1] <= rect1.top_right[1] \
            <= rect2.top_left[1] and \
            rect2.bottom_left[0] <= rect1.bottom_right[0] \
            <= rect2.bottom_right[0] and \
            rect2.bottom_left[1] <= rect1.bottom_right[1] <= rect2.top_left[1]:
        return True

    if rect2.bottom_left[0] <= rect1.top_left[0] <= rect2.bottom_right[0] and \
            rect2.bottom_left[1] <= rect1.top_left[1] <= rect2.top_left[1] and \
            rect2.bottom_left[0] <= rect1.top_right[0] \
            <= rect2.bottom_right[0] and \
            rect2.bottom_right[1] <= rect1.top_right[1] <= rect2.top_right[1]:
        return True
    return False


def point_intersection(rect1, rect2):
    for p in rect1.points():
        if p in rect2.points():
            return True
    return False


def one_corner_intersect(rect1, rect2):
    # Case Rect 1 bototm right with rect2 tp left

    if rect2.top_left[0] <= rect1.bottom_right[0] <= rect2.top_right[0] and \
            rect2.bottom_left[1] <= rect1.bottom_right[1] <= rect2.top_left[1]:
        return True

    if rect2.bottom_left[0] <= rect1.top_left[0] <= rect2.bottom_right[0] and \
            rect2.bottom_left[1] <= rect1.top_left[1] <= rect2.top_left[1]:
        return True

    return False


def subsumes(rect1, rect2):
    if rect1.top_left[0] <= rect2.top_left[0] and \
            rect1.top_left[1] >= rect2.top_left[1] and \
            rect1.bottom_right[0] >= rect2.bottom_right[0] and \
            rect1.bottom_right[1] <= rect2.bottom_right[1]:
        return True
    return False


def test_subsumes():
    assert subsumes(
        Rectangle((3, 4), (5, 2)), Rectangle((4, 4), (5, 2))) is True
    assert subsumes(
        Rectangle((4, 4), (5, 2)), Rectangle((3, 4), (5, 2))) is False


test_rectangle_intersection()
test_subsumes()
