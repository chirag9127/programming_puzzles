"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).
"""


def test():
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("CDFG", "AB") == ""


def update_min_window(found, min_window, string, window_string):
    for item in found:
        if item == -1:
            return None, ""
    new_min_window = max(found) - min(found)
    min_pos = min(found)
    max_pos = max(found)
    if not min_window:
        min_window = new_min_window
        window_string = string[min_pos:max_pos + 1]
    elif new_min_window < min_window:
        min_window = new_min_window
        window_string = string[min_pos:max_pos + 1]
    return min_window, window_string


def min_window_substring(string, substring):
    char_to_pos = {}
    min_window, window_string = None, ""
    for pos, char in enumerate(substring):
        char_to_pos[char] = pos
    found = [-1] * (len(substring))
    for pos, char in enumerate(string):
        if char in substring:
            found[char_to_pos[char]] = pos
            min_window, window_string = update_min_window(found, min_window,
                                                          string,
                                                          window_string)
    return window_string
