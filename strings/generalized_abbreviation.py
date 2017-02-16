"""
Write a function to generate the generalized abbreviations of a word.
"""
import pytest


@pytest.mark.parametrize("word,output", [
    ("word", ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2",
              "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]),
])
def test_general_abbrev(word, output):
    assert set(general_abbrev(word)) == set(output)


def general_abbrev(word):
    output = permutations(word)

    print(output)


def permutations(word):
    length = len(word)
    res = []
    res.append("") if length == 0 else res.append(str(length))
    for i in range(len(word)):
        for string in permutations(word[i + 1:]):
            left = str(i) if i > 0 else ""
            res.append(left + word[i: i + 1] + string)

    return res
