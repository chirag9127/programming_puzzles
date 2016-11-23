"""
Given a number n, return the numbers from 1 to n in lexicographix order
"""
import pytest


def lexical_order(n):
    nums = [i for i in range(1, n + 1)]
    return sorted(nums, key=lambda x: str(x))


def lexical_order_low_memory(n):
    result = []
    curr = 1
    for i in range(n):
        result.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            if curr >= n:
                curr /= 10
            curr += 1
            while curr % 10 == 0:
                curr /= 10
    return result


@pytest.mark.parametrize("n,expected_output", [
    (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_lexical_order(n, expected_output):
    assert lexical_order(n) == expected_output
    assert lexical_order_low_memory(n) == expected_output
