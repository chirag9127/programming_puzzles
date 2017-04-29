import pytest


@pytest.mark.parametrize("arr,output", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 0, -1], 2),
])
def test_longest_consecutive_subsequence(arr, output):
    assert longest_consecutive_subsequence(arr) == output


def longest_consecutive_subsequence(arr):
    parent = [i for i in range(len(arr))]
    rank = [1] * len(arr)
    pos_dict = {val: i for i, val in enumerate(arr)}
    for i, val in enumerate(arr):
        if val - 1 in pos_dict:
            union(parent, rank, i, pos_dict[val - 1])
        elif val + 1 in pos_dict:
            union(parent, rank, i, pos_dict[val + 1])
    print (parent)
    count = [0] * len(arr)
    visited = set()
    for i, val in enumerate(arr):
        if val in visited:
            continue
        visited.add(val)
        visit(parent, i, count)
    print (count)
    return max(count)


def visit(parent, x, count):
    count[x] += 1
    if parent[x] != x:
        visit(parent, parent[x], count)


def union(parent, rank, x, y):
    parent_x = find(parent, x)
    parent_y = find(parent, y)
    if parent_x == parent_y:
        return
    if rank[parent_x] > rank[parent_y]:
        parent[parent_y] = parent_x
    elif rank[parent_x] < rank[parent_y]:
        parent[parent_x] = parent_y
    else:
        parent[parent_x] = parent_y
        rank[parent_y] += 1


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# print (longest_consecutive_subsequence([0, 0, -1]))
