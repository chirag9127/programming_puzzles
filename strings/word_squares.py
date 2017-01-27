"""
Given a set of words (without duplicates),
find all word squares you can build from them.
"""
import pytest


@pytest.mark.parametrize("words,expected_output", [
    (["area", "lead", "wall", "lady", "ball"],
     [
      ["wall",
       "area",
       "lead",
       "lady"
       ],
      ["ball",
       "area",
       "lead",
       "lady"
       ]
     ]),
    (["abat", "baba", "atan", "atal"],
     [["baba",
       "abat",
       "baba",
       "atan"
       ],
      ["baba",
       "abat",
       "baba",
       "atal"
       ]]),
])
def test_word_squares(words, expected_output):
    word_squares(words) == expected_output


def make_trie(words):
    t = {}
    for word in words:
        curr = t
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = '#'
    return t


def word_squares(words):
    trie = make_trie(words)
    res = []
    word_len = len(words[0])
    for word in words:
        possible_squares_with_word(trie, word, word_len, res)
    return res


def possible_squares_with_word(trie, word, word_len, res):
    res_words = [word]
    poss(word, 1, trie, word_len, res_words, res)


def poss(word, prefix_length, trie, word_len, res_words, res):
    if prefix_length == word_len:
        res.append(res_words)
        return
    prefix = [w[prefix_length] for w in res_words]
    prefix = ''.join(prefix)
    for w in get_all_words_with_given_prefix(trie, prefix):
        r = res_words[:]
        r.append(w)
        poss(w, prefix_length + 1, trie, word_len, r, res)


def get_all_words_with_given_prefix(trie, prefix):
    words = []
    t = trie
    for char in prefix:
        if char not in t:
            return []
        t = t[char]
    get_words(t, prefix, words)
    return words


def get_words(t, word, words):
    for char in t:
        if char == '#':
            words.append(word)
            continue
        get_words(t[char], word + char, words)


def test_trie():
    words = ['are', 'area', 'arrange', 'ball', 'balls']
    trie = make_trie(words)
    assert set(get_all_words_with_given_prefix(trie, 'are')) == \
        set(['are', 'area'])
