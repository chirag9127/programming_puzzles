"""
Given a string, find the length of the longest substring T that contains
at most 2 distinct characters.
"""
import pytest


@pytest.mark.parametrize("string,output", [
    ("eceba", 3),
    ("", 0),
    ("a", 1),
    ("aa", 2),
])
def test_length_longest_substring_two_chars(string, output):
    assert length_longest_substring_two_chars(string) == output


def length_longest_substring_two_chars(string):

    if not string:
        return 0
    chars = set([string[0]])

    left = 0
    right = 1
    count_distinct = 0
    max_substring_len = 1
    while right < len(string):
        if count_distinct <= 2:
            chars.add(string[right])
            count_distinct = len(chars)
            if max_substring_len < (right - left + 1) and count_distinct <= 2:
                max_substring_len = right - left + 1
            right += 1
        else:
            distinct = set(string[left:right])
            while left <= right and len(distinct) > 2:
                left += 1
                distinct = set(string[left:right])
            chars = distinct
            count_distinct = len(chars)

    return max_substring_len
