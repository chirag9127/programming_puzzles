"""
Given a list of strings, find the pairs which are palindromes
"""


def test_palindrome_pairs():
    test1 = ["abcd", "dcba", "", "aba", "abb", "a"]
    print (palindrome_pairs(test1))
    # assert palindrome_pairs(test1) == [(0, 1), (1, 0), (2, 3), (3, 2)]


def test_palindrome():
    assert check_palindrome("bob") is True
    assert check_palindrome("s") is True
    assert check_palindrome("alpha") is False


def check_palindrome(word):
    if word == word[::-1]:
        return True
    return False


def palindrome_pairs(words):
    word_map = {}
    for i, word in enumerate(words):
        word_map[word] = i

    results = []
    for word in words:
        if word == "":
            continue
        if check_palindrome(word) and "" in word_map:
            results.append((word, ""))
            results.append(("", word))

        reverse = word[::-1]
        if reverse in word_map and word_map[reverse] != word_map[word]:
            if (word, reverse) not in results:
                results.append((word, reverse))

        for i in range(len(word)):
            left = word[0:i]
            right = word[i:]
            if check_palindrome(left):
                rev_right = right[::-1]
                if rev_right in word_map and \
                        word_map[word] != word_map[rev_right]:
                    if (word, rev_right) not in results:
                        results.append((word, rev_right))

            if check_palindrome(right):
                rev_left = left[::-1]
                if rev_left in word_map and \
                        word_map[word] != word_map[rev_left]:
                    if (word, rev_left) not in results:
                        results.append((word, rev_left))

    return results


test_palindrome()

test_palindrome_pairs()
