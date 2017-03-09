"""
Write a function to determine if the starting player can guarantee a win.
"""
import pytest


@pytest.mark.parametrize("string,output", [
    ("++++", True),
    ("+++++", False),
    ("+++++++++", False),
])
def test_flipgame(string, output):
    assert flipgame(string) == output


def flipgame(string, player1=True, cache={}):
    if (string, player1) in cache:
        return cache[(string, player1)]
    no_more_moves = True
    for i in range(len(string) - 1):
        if string[i] == '+' and string[i + 1] == '+':
            no_more_moves = False
            break
    if no_more_moves:
        sol = True if not player1 else False
        cache[(string, player1)] = sol
        return cache[(string, player1)]
    output = []
    for i in range(len(string) - 1):
        if string[i] == '+' and string[i + 1] == '+':
            new_str = string[:i] + '--' + string[i + 2:]
            output.append(flipgame(new_str, player1=not player1))
    if player1:
        sol = True if any(output) else False
    else:
        sol = True if all(output) else False
    cache[(string, player1)] = sol
    return cache[(string, player1)]
