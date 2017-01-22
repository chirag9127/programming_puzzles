"""
Given a 2D board and a list of words from the dictionary,
find all words in the board.
"""
import pytest


def word_search(words, board):
    results = []
    word_set = set(words)
    word_prefixes_set = set()
    visited = [[False for j in range(len(board[i]))]
               for i in range(len(board))]
    for word in words:
        for i in range(1, len(word) + 1):
            word_prefixes_set.add(word[:i])
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in word_prefixes_set:
                start_search(board, i, j, board[i][j], word_set,
                             word_prefixes_set, visited, results)
    return results


def start_search(board, x, y, word, word_set, word_prefixes_set, visited,
                 results):
    if visited[x][y]:
        return
    if word in word_set:
        results.append(word)
    visited[x][y] = True
    if x + 1 < len(board) and word + board[x + 1][y] in word_prefixes_set:
        start_search(board, x + 1, y, word + board[x + 1][y], word_set,
                     word_prefixes_set, visited, results)
    if x - 1 >= 0 and word + board[x - 1][y] in word_prefixes_set:
        start_search(board, x - 1, y, word + board[x - 1][y], word_set,
                     word_prefixes_set, visited, results)
    if y + 1 < len(board[x]) and word + board[x][y + 1] in word_prefixes_set:
        start_search(board, x, y + 1, word + board[x][y + 1], word_set,
                     word_prefixes_set, visited, results)
    if y - 1 >= 0 and word + board[x][y - 1] in word_prefixes_set:
        start_search(board, x, y - 1, word + board[x][y - 1], word_set,
                     word_prefixes_set, visited, results)
    visited[x][y] = False


@pytest.mark.parametrize("words,board,expected_output", [
    (["oath", "pea", "eat", "rain"],
     [
       ['o', 'a', 'a', 'n'],
       ['e', 't', 'a', 'e'],
       ['i', 'h', 'k', 'r'],
       ['i', 'f', 'l', 'v']
     ],
     ["eat", "oath"]),
    (["aaa"], [['a', 'a']], [])
])
def test_word_search(words, board, expected_output):
    assert set(word_search(words, board)) == set(expected_output)
