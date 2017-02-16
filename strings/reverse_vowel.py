"""
Write a function that takes a string as input and
reverse only the vowels of a string.
"""
import pytest


@pytest.mark.parametrize("string,reversed_string", [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
])
def test_reverse_vowels(string, reversed_string):
    assert reverse_vowels(string) == reversed_string


def reverse_vowels(string):
    string = list(string)
    start = 0
    end = len(string) - 1

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    while start < end:
        if string[start] in vowels and string[end] in vowels:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
            continue
        if string[start] not in vowels:
            start += 1
            continue
        if string[end] not in vowels:
            end -= 1

    return ''.join(string)
