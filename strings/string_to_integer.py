"""
Convert a string to an integer if possible
"""


def test():
    try:
        string_to_integer('aaa')
    except ValueError:
        print "Reached HERE"
        assert True
        pass
    assert string_to_integer('1234') == 1234
    try:
        string_to_integer(' 5678')
    except ValueError:
        print "Reached HERE 1"
        assert True
        pass
    try:
        string_to_integer('12.34')
    except ValueError:
        print "Reached HERE 2"
        assert True
        pass
    assert string_to_integer('-1234') == -1234


def string_to_integer(string):
    num = 0
    neg = False
    if string[0] == '-':
        neg = True
        string = string[1:]
    for char in string:
        if char < '0' or char > '9':
            raise ValueError
        num *= 10
        num += ord(char) - ord('0')
    if neg:
        num *= -1
    return num
