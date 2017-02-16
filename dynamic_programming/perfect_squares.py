"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.
"""
import pytest


@pytest.mark.parametrize("n,output", [
    (12, 3),
    (13, 2),
])
def test_perfect_squares(n, output):
    assert perfect_squares(n) == output


def perfect_squares(n):
    squares = []

    # Generate all squares till n

    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    min_squares = [0, 1]

    for i in range(2, n + 1):
        curr_min = 99999
        for square in squares:
            if i >= square:
                curr_min = min(curr_min, min_squares[i - square] + 1)
            else:
                break
        min_squares.append(curr_min)

    return min_squares[-1]
