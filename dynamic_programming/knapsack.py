import pytest


@pytest.mark.parametrize("array,k,output", [
    ([1, 4, 5], 3, False),
    ([2, 3, 5, 7], 5, True),
    ([5, 7, 6, 2, 3], 15, True),
])
def test_knapsack(array, k, output):
    assert knapsack(array, k) == output


def knapsack(array, k):
    dp = [[False] * (len(array) + 1) for _ in range(k + 1)]
    dp[0][0] = True
    for i in range(k + 1):
        for j, item in enumerate(array):
            dp[i][j + 1] = True if i - item >= 0 and \
                dp[i - item][j] is True or \
                dp[i][j] is True else False
    return dp[-1][-1]


if __name__ == "__main__":
    knapsack([2, 3, 5, 7], 5)
