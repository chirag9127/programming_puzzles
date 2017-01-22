"""
Reverse bits of a given 32 bits unsigned integer.
"""
import pytest


@pytest.mark.parametrize("num,output", [
    (43261596, 964176192),
])
def test_reverse_bits(num, output):
    assert reverse_bits(num) == output


def reverse_bits(num):
    return int(bin(num)[2:].zfill(32)[::-1], 2)
