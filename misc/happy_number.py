"""
Write an algorithm to determine if a number is "happy".
"""
import pytest


@pytest.mark.parametrize("num,expected_output", [
    (19, True),
])
def test_happy_number(num, expected_output):
    assert happy_number(num) == expected_output


def happy_number(num):
    seen = set()
    while True:
        if num in seen:
            return False
        seen.add(num)
        if num == 1:
            return True
        new_num = 0
        while num > 0:
            rem = num % 10
            new_num += rem * rem
            num = num / 10
        num = new_num
