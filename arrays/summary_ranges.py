"""
Given a sorted integer array without duplicates,
return the summary of its ranges.
"""
import pytest


@pytest.mark.parametrize("array,output", [
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 5, 7], ["0", "2->5", "7"]),
])
def test_summary_ranges(array, output):
    assert summary_ranges(array) == output


def summary_ranges(array):
    curr = (array[0], None)
    output = []
    for i in range(1, len(array)):
        if array[i] == array[i - 1] + 1:
            curr = (curr[0], array[i])
        else:
            if not curr[1]:
                output.append(str(curr[0]))
            else:
                output.append("{0}->{1}".format(curr[0], curr[1]))
            curr = (array[i], None)
    if not curr[1]:
        output.append(str(curr[0]))
    else:
        output.append("{0}->{1}".format(curr[0], curr[1]))

    return output
