"""
Given a target string and a set of strings in a dictionary, find an
abbreviation of this target string with the smallest possible length such that
it does not conflict with abbreviations of the strings in the dictionary.
"""
import pytest


@pytest.mark.parametrize("word,word_set,output", [
    ("apple", ["blade"], "a4"),
    ("apple", ["plain", "amber", "blade"], "ap3"),
])
def test_min_unique_abbreviation(word, word_set, output):
    assert min_unique_abbreviation(word, word_set) == output


def min_unique_abbreviation(word, word_set):
    all_abbrevs = []
    for w in word_set:
        abbrevs = get_abbrevs(w)
        all_abbrevs.extend(abbrevs)
    all_abbrevs = set(all_abbrevs)

    abbrevs_for_candidate = get_abbrevs(word)
    abbrevs_for_candidate.sort(key=lambda x: len(x))
    for candidate in abbrevs_for_candidate:
        if candidate not in all_abbrevs:
            return candidate

    return -1


def get_abbrevs(word):
    length = len(word)
    res = []
    res.append("") if length == 0 else res.append(str(length))
    for i in range(len(word)):
        for string in get_abbrevs(word[i + 1:]):
            left = str(i) if i > 0 else ""
            res.append(left + word[i: i + 1] + string)

    return res


print (min_unique_abbreviation("apple", ["plain", "amber", "blade"]))
