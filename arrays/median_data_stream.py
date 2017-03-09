"""
Design a data structure for finding median in a stream
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        self.large = []
        self.small = []

    def add_num(self, num):
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def get_median(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0


def test_median_finder():
    mf = MedianFinder()
    mf.add_num(1)
    assert mf.get_median() == 1

    mf.add_num(2)
    assert mf.get_median() == 1.5

    mf.add_num(3)
    assert mf.get_median() == 2

    mf.add_num(4)
    assert mf.get_median() == 2.5

    mf = MedianFinder()
    mf.add_num(-1)
    mf.add_num(-2)
    assert mf.get_median() == -1.5

    mf.add_num(-3)
    assert mf.get_median() == -2


test_median_finder()
