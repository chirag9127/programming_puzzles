"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
import pytest
import re


def is_palindrome(string):
    # Remove all the non alphanumeric characters
    string = re.sub(r'\W+', '', string).lower()
    for i in range(len(string)/2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


@pytest.mark.parametrize("string,palindrome", [
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
])
def test_is_palindrome(string, palindrome):
    assert is_palindrome(string) == palindrome
