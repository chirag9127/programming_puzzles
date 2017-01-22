"""
Given a sanitized token, find all possible original tokens
"""
import pytest


@pytest.mark.parametrize("word,expected_output", [
    ("ab", ["Ab", "AB", "aB", "ab"]),
    ("abc", ["Abc", "aBc", "abC", "ABc", "AbC", "aBC", "ABC", "abc"]),
    ("ab7c", ["Ab7c", "aB7c", "ab7C", "AB7c", "Ab7C", "aB7C", "AB7C", "ab7c"])
])
def test_decode_string(word, expected_output):
    assert set(decode_string(word)) == set(expected_output)


def decode_string(word):
    res = []
    get_combinations(word, 0, res)
    return res


def get_combinations(word, pos, res):
    if pos == len(word):
        res.append(word)
        return
    if word[pos].isdigit():
        get_combinations(word, pos + 1, res)
        return
    if word[pos].lower():
        get_combinations(word, pos + 1, res)
        word = word[:pos] + word[pos].upper() + word[pos + 1:]
        get_combinations(word, pos + 1, res)
    else:
        get_combinations(word, pos + 1, res)
        word = word[:pos] + word[pos].lower() + word[pos + 1:]
        get_combinations(word, pos + 1, res)
