"""
For two strings A and B we define string similarity as the length of the
longest common prefix.
Calculate the sum of similarities of string S with each of its suffixes
"""
import pytest


@pytest.mark.parametrize("inputs,expected_output", [
    (["ababaa"], [11]),
    (["aa"], [3]),
])
def test_string_similarity(inputs, expected_output):
    assert string_similarity(inputs) == expected_output


def string_similarity(inputs):
    output = []
    for item in inputs:
        string_similarity_sum = len(item)
        for i in range(1, len(item)):
            string_similarity_sum += lcp(item, item[i:])

        output.append(string_similarity_sum)

    return output


def lcp(stringA, stringB):
    lcp_length = 0
    for i in range(len(stringB)):
        if stringA[i] != stringB[i]:
            return lcp_length
        lcp_length += 1
    return lcp_length


@pytest.mark.parametrize("stringA,stringB,output", [
    ('abc', 'abd', 2),
    ('aaab', 'aaa', 3),
])
def test_lcp(stringA, stringB, output):
    assert lcp(stringA, stringB) == output
