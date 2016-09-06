"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
import pytest


def climb_stairs(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 2
    item1 = 1
    item2 = 2
    for i in range(3, num + 1):
        item3 = item1 + item2
        item1 = item2
        item2 = item3
    return item3


@pytest.mark.parametrize("num,expected_output", [
    (1, 1),
    (4, 5),
    (3, 3),
])
def test_climb_stairs(num, expected_output):
    assert climb_stairs(num) == expected_output
