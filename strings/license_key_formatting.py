"""
Format a given license key.
"""
import pytest


@pytest.mark.parametrize("string,k,expected_output", [
    ("2-4A0r7-4k", 4, "24A0-R74K"),
    ("2-4A0r7-4k", 3, "24-A0R-74K"),
])
def test_license_key_formatting(string, k, expected_output):
    assert license_key_formatting(string, k) == expected_output


def license_key_formatting(string, k):
    string = string.replace('-', '')
    string = string[::-1].upper()
    i = k
    while i < len(string):
        string = string[:i] + '-' + string[i:]
        i += k + 1
    return string[::-1]
