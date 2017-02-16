"""
Given a non-empty string, encode the string such that its encoded
length is the shortest.
"""
import pytest


@pytest.mark.parametrize("string,output", [
    ("aaa", "aaa"),
    ("aaaaa", "5[a]"),
    ("aaaaaaaaaa", "10[a]"),
    ("aabcaabcd", "2[aabc]d"),
    ("abbbabbbcabbbabbbc", "2[2[abbb]c]"),
])
def test_encode_string(string, output):
    assert encode(string) == output


def encode(string, memo={}):
    if string not in memo:
        n = len(string)
        i = (string + string).find(string, 1)
        one = '%d[%s]' % (n / i, encode(string[:i])) if i < n else string
        multi = [encode(string[:j]) + encode(string[j:]) for j in range(1, n)]
        memo[string] = min([string, one] + multi, key=len)

    return memo[string]
