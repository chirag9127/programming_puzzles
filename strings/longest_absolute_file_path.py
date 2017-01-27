"""
Find the longest absolute file path
"""
import pytest


@pytest.mark.parametrize("string,expected_output", [
    ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
    ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t"
     "subsubdir2\n\t\t\tfile2.ext", 32),
    ("dir\nfile.txt", 8),
])
def test_longest_absolute_file_path(string, expected_output):
    assert longest_absolute_file_path(string) == expected_output


def longest_absolute_file_path(string):
    string = string.split('\n')
    pos_to_lengths = {}
    max_length = 0
    for i in range(len(string)):
        item = string[i]
        count_tabs = 0
        while item.startswith('\t'):
            count_tabs += 1
            item = item[1:]
        if count_tabs == 0:
            curr_length = len(item)
        else:
            curr_length = pos_to_lengths[count_tabs] + len(item) + 1
        pos_to_lengths[count_tabs + 1] = curr_length
        if '.' in item:
            if curr_length > max_length:
                max_length = curr_length
    return max_length
