"""
Implement regular expression matching with support for '.' and '*'.
"""
import pytest


def regex_matching(string, pattern):
    print string, pattern
    # Case 1: Both the string and pattern are extinguished
    if not string and not pattern:
        return True

    # Case 2: String is present, pattern extinguished
    if string and not pattern:
        return False

    # Handling the * cases
    if len(pattern) > 1 and pattern[1] == '*':
        if len(pattern) > 3 and pattern[3] == '*':
            # a*a* = a*
            if pattern[0] == pattern[2]:
                return regex_matching(string, pattern[2:])
            # .*a* = .*
            if pattern[0] == '.':
                return regex_matching(string, '.' + pattern[3:])
        # zero match
        ret = regex_matching(string, pattern[2:])

        if not string:
            pass
        elif string[0] == pattern[0]:
            ret = ret or regex_matching(string[1:], pattern)
        elif pattern[0] == '.':
            ret = ret or regex_matching(string[1:], pattern) or \
                regex_matching('', pattern[2:])
        return ret
    elif (string and string[0] == pattern[0]) or (string and pattern[0] == '.'):
        return regex_matching(string[1:], pattern[1:])

    return False


@pytest.mark.parametrize("string,pattern,expected_output", [
    ("aa", "a", False),
    ("aa", "aa", True),
    ("aaa", "aa", False),
    ("aa", "a*", True),
    ("aa", ".*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("ab", ".*c", False),
    ("bbbba", ".*a*a", True),
])
def test_regex_matching(string, pattern, expected_output):
    assert regex_matching(string, pattern) == expected_output
