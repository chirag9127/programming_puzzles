"""
Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.
"""
import pytest


@pytest.mark.parametrize("n,expected_output", [
    (1, ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02",
         "0:04", "0:08", "0:16", "0:32"]),
])
def test_binary_watch(n, expected_output):
    assert set(binary_watch(n)) == set(expected_output)


def convert_leds_to_time(leds):
    hours = leds[:4]
    minutes = leds[4:]
    hour_int = sum([val * pow(2, (4 - i - 1))
                    for i, val in enumerate(hours)])
    if hour_int > 11:
        return None
    minute_int = sum([val * pow(2, (6 - i - 1))
                      for i, val in enumerate(minutes)])
    if minute_int > 59:
        return None
    if minute_int < 10:
        return "{0}:0{1}".format(hour_int, minute_int)
    return "{0}:{1}".format(hour_int, minute_int)


def binary_watch(n):
    leds = [0] * 10
    for i in range(n):
        leds[i] = 1
    end_state = [0] * 10
    for i in range(n):
        end_state[10 - i - 1] = 1
    # curr = convert_leds_to_time(leds)
    res = []
    for item in get_permutations(leds, 0):
        print (item)
        time = convert_leds_to_time(item)
        if time:
            res.append(time)
    print (res)
    return res


def get_combinations(leds, end_state):
    yield leds
    for i in range(len(leds)):
        if leds[i] == 1 and leds[i + 1] == 0:
            break
    right_most = i
    leds[right_most] = 0
    for i in range(right_most + 1, len(leds)):
        if leds[i] == 1:
            i -= 1
            break
        else:
            leds[i] = 1
            yield leds
            leds[i] = 0
    leds[i] = 1
    if leds == end_state:
        return
    for item in get_combinations(leds, end_state):
        yield item


def get_permutations(leds, pos):
    if pos == len(leds) - 1:
        yield tuple(leds)
        return
    for i in range(len(leds)):
        if leds[pos] == leds[i]:
            continue
        leds[pos], leds[i] = leds[i], leds[pos]
        for item in get_permutations(leds, pos + 1):
            yield tuple(item)
        leds[pos], leds[i] = leds[i], leds[pos]


# print (set(get_permutations([0, 1, 2], 0)))


binary_watch(5)
