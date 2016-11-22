"""
Given an integer reverse the digits
"""
import pytest


@pytest.mark.parametrize("num,expected_output", [
    (123, 321),
    (-123, -321),
])
def test_reverse(num, expected_output):
    assert reverse(num) == expected_output


def sign(num):
    return -1 if num < 0 else 1


def reverse(num):
    sgn = sign(num)
    num = abs(num)
    output = 0
    while num:
        output *= 10
        rem = num % 10
        output += rem
        num = num / 10
    return output
