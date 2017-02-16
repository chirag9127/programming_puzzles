"""
Given an Android 3x3 key lock screen and two integers m and n,
where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the
Android lock screen, which consist of minimum of m keys and maximum n keys.
"""
import pytest


@pytest.mark.parametrize("m,n,num_patterns", [
    (1, 1, 9),
])
def test_android_unlock_patterns(m, n, num_patterns):
    assert android_unlock_patterns(m, n) == num_patterns


def android_unlock_patterns(m, n):
    skips = [[0 for j in range(10)] for i in range(10)]

    skips[1][3] = skips[3][1] = 2
    skips[1][7] = skips[7][1] = 4
    skips[7][9] = skips[9][7] = 8
    skips[9][3] = skips[3][9] = 6
    skips[1][9] = skips[3][7] = skips[2][8] = skips[4][6] = 5
    skips[9][1] = skips[7][3] = skips[8][2] = skips[6][4] = 5

    res = 0
    visited = [False for i in range(1, 10)]
    for i in range(m, n + 1):
        res += dfs(1, i - 1, visited, skips) * 4
        res += dfs(2, i - 1, visited, skips) * 4
        res += dfs(5, i - 1, visited, skips)

    return res


def dfs(num, remaining, visited, skips):
    if remaining == 0:
        return 1

    count = 0
    visited[num - 1] = True

    for i in range(1, 10):
        if not visited[i - 1] and \
                (skips[num][i] == 0 or visited[skips[num][i] - 1]):
            count += dfs(i, remaining - 1, visited, skips)

    visited[num - 1] = False

    return count
