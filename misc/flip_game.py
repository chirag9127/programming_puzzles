"""
Given the a string which contains only '+', '-'. Generate all possible states
by converting '++' to '--'
"""
import pytest


@pytest.mark.parametrize("string,output", [
    ('++++', ['--++', '+--+', '++--']),
])
def test_flip_game(string, output):
    assert set(flip_game(string)) == set(output)


def flip_game(string):
    result = []
    for i in range(len(string) - 1):
        if string[i] == '+' and string[i + 1] == '+':
            result.append(string[:i] + '--' + string[i + 2:])
    return result
