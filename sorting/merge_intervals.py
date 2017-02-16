"""
Given a collection of intervals, merge all overlapping intervals.
"""
import pytest


@pytest.mark.parametrize("intervals,output", [
    ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
])
def test_merge_intervals(intervals, output):
    assert merge_intervals(intervals) == output


def merge_intervals(intervals):
    times = []
    for item in intervals:
        times.append((item[0], True))
        times.append((item[1], False))
    times.sort(key=lambda x: (x[0], not x[1]))
    count_start = 0
    output = []
    curr = ()
    for time in times:
        if time[1] is False:
            count_start -= 1
            if count_start == 0:
                curr = (curr[0], time[0])
                output.append(curr)
                curr = ()
        elif time[1] is True:
            if count_start == 0:
                curr = (time[0], None)
            count_start += 1
    return output
