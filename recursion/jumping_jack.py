"""
Jumping Jack. Write a function to find the maximum step reachable from step 0
using n actions and never jumping on step k.
"""
import pytest


@pytest.mark.parametrize("n,k,expected_output", [
    (2, 2, 3),
    (2, 1, 2),
    (3, 3, 5),
    (3, 25, 6),
    (4, 1, 9),
])
def test_jumping_jack(n, k, expected_output):
    """
    Tests for jumping_jack_method
    """
    assert jumping_jack(n, k) == expected_output


def jumping_jack(n, k):
    res = 0
    visited_k = False
    for i in range(1, n + 1):
        res += i
        if res == k:
            visited_k = True

    if visited_k:
        return res - 1
    return res
