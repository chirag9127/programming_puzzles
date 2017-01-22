"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""
import pytest


@pytest.mark.parametrize("string,expected_output", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("(())", True),
    ("(", False),
])
def test_valid_parenthesis(string, expected_output):
    assert valid_parenthesis(string) == expected_output


def valid_parenthesis(string):
    stack = []
    bracket_pairs = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [']', ')', '}']:
            if len(stack) == 0:
                return False
            top = stack[-1]
            if top != bracket_pairs[char]:
                return False
            stack.pop()
    if len(stack) > 0:
        return False
    return True
