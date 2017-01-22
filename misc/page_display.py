"""
Given a list of cities and a limit, print only unique cities by limit.
"""
import pytest


def page_display(words, limit):
    curr_set = set()
    curr_line = []
    res = []
    i = 0
    while len(words) > 0:
        if words[i] not in curr_set:
            curr_line.append(words[i])
            curr_set.add(words[i])
            words.pop(i)
        else:
            i += 1
        if len(curr_line) == limit or i == len(words):
            curr_set = set()
            res.append(curr_line)
            curr_line = []
            i = 0
    return res


@pytest.mark.parametrize("words,limit,expected_output", [
    (["SFO", "Chicago", "SFO", "NYC", "Berlin"], 3,
     [["SFO", "Chicago", "NYC"],
      ["SFO", "Berlin"]])
])
def test_page_display(words, limit, expected_output):
    assert page_display(words, limit) == expected_output
