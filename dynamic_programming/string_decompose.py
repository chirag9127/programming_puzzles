"""
Given a string without spaces and a dictionary, check if the string
can be decomposed into words of the dictionary
"""
import pytest


def string_decompose(string, dictionary):
    string_marker = [False for i in range(len(string))]
    for i in range(len(string) + 1):
        if string[0:i] in dictionary:
            string_marker[i - 1] = True
            continue
        for j in range(i):
            if string_marker[j] is True and string[j+1:i] in dictionary:
                string_marker[i - 1] = True
                break
    return string_marker[-1]


@pytest.mark.parametrize("string,dictionary,expected_output", [
    ('ilovemangoes', set(['i', 'love', 'mango']), False),
    ('ilovemangoes', set(['i', 'love', 'mango', 'goes']), False),
    ('ilovemangoes', set(['i', 'love', 'mangoes', 'goes']), True),
    ('ilovemangoes', set(['i', 'love', 'man', 'goes']), True),
])
def test_string_decomposition(string, dictionary, expected_output):
    assert string_decompose(string, dictionary) == expected_output
