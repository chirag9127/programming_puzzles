"""
Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.
"""
import pytest


@pytest.mark.parametrize("citations,output", [
    ([3, 0, 6, 1, 5], 3),
])
def test_h_index(citations, output):
    assert h_index(citations) == output


def h_index(citations):
    citations = sorted(citations)
    curr_h_index = 0
    for i in range(len(citations)):
        curr = len(citations) - i
        if citations[i] >= curr:
            curr_h_index = curr
            return curr_h_index
    return 0


print (h_index([3, 0, 6, 1, 5]))
