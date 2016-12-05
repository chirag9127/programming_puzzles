"""
Given a matrix find all the pairs of numbers which sum up to a given input
sum. The numbers may not be in the same row.
E.g.
 1  3  2  4
 5  8  7  6
 9 10 13 11
12  0 14 15
The given sum is 11.
The possible pairs are (1, 10), (3, 8), (2, 9), (4, 7), (1, 11)
"""


def test_sum_in_matrix():
    matrix = [[1, 3, 2, 4], [5, 8, 7, 6], [9, 10, 13, 11], [12, 0, 14, 15]]
    assert sum_in_matrix(matrix, 11) == set([(1, 10), (3, 8), (2, 9),
                                             (4, 7), (0, 11)])


nodes = {}


class Node(object):

    def __init__(self, val, row, column):
        self.val = val
        self.row = row
        self.column = column
        if self.val not in nodes:
            nodes[self.val] = []
        nodes[self.val].append((self.row, self.column))


def sum_in_matrix(matrix, tot_sum):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            node = Node(matrix[i][j], i, j)
    solution = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if tot_sum - matrix[i][j] in nodes:
                start = nodes[matrix[i][j]]
                end = nodes[tot_sum - matrix[i][j]]
                for k in start:
                    for p in end:
                        if k[0] == p[0]:
                            continue
                        lesser = matrix[i][j] \
                            if matrix[i][j] <= tot_sum - matrix[i][j] \
                            else tot_sum - matrix[i][j]
                        greater = tot_sum - lesser
                        solution.add((lesser, greater))
    return solution
