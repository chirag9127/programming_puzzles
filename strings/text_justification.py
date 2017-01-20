"""
Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.
"""
import pytest


def text_justification(words, max_width):
    result = []
    curr_length = 0
    curr_line = []
    for word in words:
        if curr_length + len(word) + len(curr_line) > max_width:
            num_remaining_spaces = max_width - curr_length
            count = 0
            while count < num_remaining_spaces:
                curr_line[
                    count % (len(curr_line) - 1 or 1)] += ' '
                count += 1
            result.append(''.join(curr_line))
            curr_line = []
            curr_length = 0
        curr_line.append(word)
        curr_length += len(word)
    result.append(' '.join(curr_line) +
                  ' '*(max_width - curr_length - len(curr_line) + 1))
    return result


@pytest.mark.parametrize("words,max_width,expected_output", [
    (["This", "is", "an", "example", "of", "text", "justification."],
     16,
     ["This    is    an", "example  of text", "justification.  "])
])
def test_text_justification(words, max_width, expected_output):
    assert text_justification(words, max_width) == expected_output
