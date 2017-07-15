import pytest


@pytest.mark.parametrize("string,output", [
    ('abc', 'a'),
    ('abcb', 'bcb'),
    ('abccb', 'bccb'),
])
def test_palindromic_substring(string, output):
    assert longest_palindromic_substring(string) == output


def longest_palindromic_substring(string):
    maxlen, left, right = 0, 0, 0
    for i, char in enumerate(string):
        k = 1
        while i - k >= 0 and i + k < len(string) and \
                string[i - k] == string[i + k]:
            k += 1
        if 2 * k - 1 > maxlen:
            maxlen = 2 * k - 1
            left = i - k + 1
            right = i + k
        if i + 1 < len(string) and string[i] == string[i + 1]:
            while i - k >= 0 and i + k + 1 < len(string) and \
                    string[i - k] == string[i + k + 1]:
                k += 1
            if 2 * k > maxlen:
                maxlen = 2 * k
                left = i - k + 1
                right = i + k + 1
    print (maxlen, string[left:right])


longest_palindromic_substring('abbacd')
