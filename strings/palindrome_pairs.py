"""
Given a list of unique words, find all pairs of distinct indices (i, j)
in the given list, so that the concatenation of the two words,
i.e. words[i] + words[j] is a palindrome.
"""
import pytest


def palindrome_pairs(words):
    word_map = {}
    results = []
    for i, word in enumerate(words):
        word_map[word] = i
    for word in words:
        if word == "":
            continue
        if is_palindrome(word):
            if "" in word_map:
                results.append([word_map[word], word_map[""]])
                results.append([word_map[""], word_map[word]])
        rev_word = word[::-1]
        if rev_word in word_map and word_map[rev_word] != word_map[word]:
            new_res = [word_map[word], word_map[rev_word]]
            if new_res not in results:
                results.append(new_res)
        for i in range(len(word)):
            left = word[0:i]
            right = word[i:]
            if is_palindrome(left):
                rev_right = right[::-1]
                if rev_right in word_map and \
                        word_map[word] != word_map[rev_right]:
                    new_res = [word_map[rev_right], word_map[word]]
                    if new_res not in results:
                        results.append(new_res)
            if is_palindrome(right):
                rev_left = left[::-1]
                if rev_left in word_map and \
                        word_map[word] != word_map[rev_left]:
                    new_res = [word_map[word], word_map[rev_left]]
                    if new_res not in results:
                        results.append(new_res)
    return results


def is_palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return True
    return False


@pytest.mark.parametrize("words,expected_output", [
    (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
    (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
])
def test_palindrome_pairs(words, expected_output):
    assert palindrome_pairs(words) == expected_output


@pytest.mark.parametrize("word,palindrome", [
    ("bob", True),
    ("cook", False),
    ("toot", True),
])
def test_is_palindrome(word, palindrome):
    assert is_palindrome(word) == palindrome


print palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
