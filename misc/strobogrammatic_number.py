"""
A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).
"""
import pytest


@pytest.mark.parametrize("num,output", [
    ("69", True),
    ("88", True),
    ("818", True),
    ("18", False),
])
def test_strobogrammatic_number(num, output):
    assert strobogrammatic_number(num) is output


def strobogrammatic_number(num):
    return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)))
