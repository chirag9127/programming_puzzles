"""
Design a hit counter which counts the number of hits received in the past
5 minutes.
"""
from collections import deque


def test_hit_counter():
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    assert obj.get_hits(4) == 3

    obj.hit(300)
    assert obj.get_hits(300) == 4
    assert obj.get_hits(301) == 3


class HitCounter(object):

    def __init__(self):
        self.queue = deque()
        self.num_hits = 0

    def hit(self, timestamp):
        if not self.queue or self.queue[-1][0] != timestamp:
            self.queue.append((timestamp, 1))
        else:
            self.queue[-1][1] += 1

        self.num_hits += 1

    def get_hits(self, timestamp):
        while self.queue and self.queue[0][0] <= timestamp - 300:
            self.num_hits -= self.queue.popleft()[1]

        return self.num_hits
