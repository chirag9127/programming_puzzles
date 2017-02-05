"""
Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer.
"""
import pytest


@pytest.mark.parametrize("array,expected_output", [
    ([0], [1]),
    ([1, 1], [1, 2]),
])
def test_plus_one(array, expected_output):
    assert plus_one(array) == expected_output


def plus_one(array):
    carry = 1
    out = []
    for i in range(len(array) - 1, -1, -1):
        digit_sum = array[i] + carry
        carry = digit_sum // 10
        out.append(digit_sum % 10)
    if carry > 0:
        out.append(carry)
    return out[:: -1]
