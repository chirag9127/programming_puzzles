"""
Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character
"""
import pytest


def edit_distance(word1, word2):
    mat = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
    for i in range(len(word1) + 1):
        mat[0][i] = i
    for j in range(len(word2) + 1):
        mat[j][0] = j
    for j in range(len(word2)):
        for i in range(len(word1)):
            if word1[i] == word2[j]:
                mat[j + 1][i + 1] = mat[j][i]
            else:
                mat[j + 1][i + 1] = min(mat[j][i],
                                        mat[j][i + 1],
                                        mat[j + 1][i]) + 1
    return mat[-1][-1]


@pytest.mark.parametrize("word1,word2,expected_output", [
    ('as', 'seven', 5),
    ('seven', 'sevet', 1),
    ('seven', 'seven', 0),
])
def test_edit_distance(word1, word2, expected_output):
    assert edit_distance(word1, word2) == expected_output


print(edit_distance("extra", "zebra"))
