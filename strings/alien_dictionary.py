"""
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.
"""
import collections
import pytest


def alien_dictionary(words):
    chars = set("".join(words))
    degree = {x: 0 for x in chars}
    graph = collections.defaultdict(list)
    for pair in zip(words, words[1:]):
        for char_x, char_y in zip(*pair):
            if char_x != char_y:
                graph[char_x].append(char_y)
                degree[char_y] += 1
                break
        if char_x == char_y and len(pair[0]) > len(pair[1]): return ""
    queue = filter(lambda x: degree[x] == 0, degree.keys())
    res = ""
    while queue:
        x = queue.pop()
        res += x
        for n in graph[x]:
            degree[n] -= 1
            if degree[n] == 0:
                queue.append(n)
    return res * (set(res) == chars)


@pytest.mark.parametrize("words,expected_output", [
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["ab", "adc"], "acbd"),
    (["wrtkj", "wrt"], ""),
    (["z", "z"], "z"),
    (["za", "zb", "ca", "cb"], "azbc")
])
def test_alien_dictionary(words, expected_output):
    assert alien_dictionary(words) == expected_output
