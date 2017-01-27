"""
Given a string, find the length of the longest substring T that
contains at most k distinct characters.
"""
import pytest


@pytest.mark.parametrize("string,k,expected_output", [
    ("eceba", 2, 3),
])
def test_longest_substring_with_atmost_k_chars(string, k, expected_output):
    assert longest_substring_with_atmost_k_chars(string, k) == \
        expected_output


def longest_substring_with_atmost_k_chars(string, k):
    d = {}
    res = 0
    low = 0
    for i, char in enumerate(string):
        d[char] = i
        if len(d) > k:
            low = min(d.values())
            del d[string[low]]
            low += 1
        res = max(res, i - low + 1)
    return res
