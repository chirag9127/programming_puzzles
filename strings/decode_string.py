"""
Given an encoded string, return it's decoded string.
"""
import pytest


@pytest.mark.parametrize("string,decoded_string", [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("sd2[f2[e]g]i", "sdfeegfeegi"),
])
def test_decode_string(string, decoded_string):
    assert decode_string(string) == decoded_string


def decode_string(string):
    stack = []
    res = ""
    i = 0
    num_count = 0
    bracket_count = 0
    curr_string = ""
    while i < len(string):
        while string[i] >= '0' and string[i] <= '9':
            num_count = num_count * 10 + int(string[i])
            i += 1
        if string[i] == '[':
            j = i + 1
            while j < len(string) and string[j] >= 'a' and string[j] <= 'z':
                curr_string += string[j]
                j += 1
            bracket_count += 1
            stack.append((num_count, curr_string))
            curr_string = ""
            num_count = 0
            i = j
        if string[i] == ']':
            out_num_count, out_string = stack.pop()
            bracket_count -= 1
            if bracket_count == 0:
                res += out_string * out_num_count
                i += 1
            else:
                next_num_count, next_string = stack.pop()
                next_string += out_string * out_num_count
                j = i + 1
                while j < len(string) and string[j] >= 'a' and string[j] <= 'z':
                    next_string += string[j]
                    j += 1
                stack.append((next_num_count, next_string))
                i = j
        if i < len(string) and string[i] >= 'a' and string[i] <= 'z':
            res += string[i]
            i += 1
    return res


print(decode_string("sd2[f2[e]g]i"))
