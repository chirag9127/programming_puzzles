"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).
"""
import collections
import pytest


@pytest.mark.parametrize("s,t,expected_output", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("abaa", "aa", "aa"),
    ("aaba", "aa", "aa")
])
def test_min_window_substring(s, t, expected_output):
    assert min_window_substring(s, t) == expected_output
    assert min_window(s, t) == expected_output


def min_window(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        print j, c
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                print "i, j", i, j, s[i], need[s[i]]
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]


min_window("ADOBECODEBANC", "ABC")


def check_window_exists(all_pos, t):
    if len(all_pos) == len(t):
        return True
    return False


def get_window_size(all_pos):
    return all_pos[-1] - all_pos[0], all_pos[0], all_pos[-1]


def update(found, t_dict, char, pos, all_pos):
    if len(found[char]) < t_dict[char]:
        found[char].add(pos)
        all_pos.append(pos)
    else:
        min_pos = min(found[char])
        found[char].remove(min_pos)
        found[char].add(pos)
        all_pos.remove(min_pos)
        all_pos.append(pos)


def min_window_substring(s, t):
    t_dict = {}
    found = {}
    for c in t:
        if c not in t_dict:
            t_dict[c] = 0
            found[c] = set()
        t_dict[c] += 1
    window_size = 9999
    window_exists = False
    window_low = None
    window_high = None
    all_pos = []
    for i, char in enumerate(s):
        if char in t:
            update(found, t_dict, char, i, all_pos)
            if window_exists or check_window_exists(all_pos, t):
                window_exists = True
                new_ws, low, high = get_window_size(all_pos)
                if new_ws < window_size:
                    window_size = new_ws
                    window_low = low
                    window_high = high
    return s[window_low: window_high + 1] if window_low is not None else ""
