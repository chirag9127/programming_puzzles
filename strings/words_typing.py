"""
Given a rows x cols screen and a sentence represented by a list of
non-empty words, find how many times the given sentence
can be fitted on the screen.
"""
import pytest


@pytest.mark.parametrize("row,col,sentence,expetcted_output", [
    (2, 8, ["hello", "world"], 1),
    (3, 6, ["a", "bcd", "e"], 2),
    (4, 5, ["I", "had", "apple", "pie"], 1),
    (2, 6, ["a", "bc"], 2),
])
def test_word_typing(row, col, sentence, expetcted_output):
    assert word_typing(row, col, sentence) == expetcted_output


def word_typing(row, col, sentence):
    word_nums = preprocess(col, sentence)
    count = 0
    for _ in xrange(row):
        count += word_nums[count % len(sentence)]
    return count / len(sentence)


def preprocess(col, sentence):
    word_nums = [0] * len(sentence)
    curr = 0
    word_len = len(sentence[0])
    word_ptr = 0
    for i, word in enumerate(sentence):
        while curr + word_len <= col:
            curr = curr + word_len
            word_ptr += 1
            word_len = len(sentence[word_ptr % len(sentence)]) + 1
        word_nums[i] = word_ptr - i
        curr -= (len(word) + 1)
    return word_nums


print preprocess(6, ["a", "bc"])
