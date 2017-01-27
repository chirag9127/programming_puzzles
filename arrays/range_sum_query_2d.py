"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle
defined by its upper left corner (row1, col1) and
lower right corner (row2, col2).
"""
from binary_indexed_tree import BinaryIndexedTree2D


class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.range_matrix = [[0 for j in range(len(self.matrix[0]))]
                             for i in range(len(self.matrix))]
        self.range_matrix[0][0] = self.matrix[0][0]
        for i in range(1, len(self.matrix)):
            self.range_matrix[i][0] = self.range_matrix[i - 1][0] + \
                self.matrix[i][0]
        for j in range(1, len(self.matrix[0])):
            self.range_matrix[0][j] = self.range_matrix[0][j - 1] + \
                self.matrix[0][j]
        for i in range(1, len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                self.range_matrix[i][j] = self.range_matrix[i][j - 1] + \
                    self.range_matrix[i - 1][j] - \
                    self.range_matrix[i - 1][j - 1] + self.matrix[i][j]

    def update(self, row, col, val):
        old = self.matrix[row][col]
        for i in range(row, len(self.matrix)):
            for j in range(col, len(self.matrix[0])):
                self.range_matrix[i][j] += val - old
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        if row1 == 0 and col1 == 0:
            return self.range_matrix[row2][col2]
        if row1 == 0:
            return self.range_matrix[row2][col2] - \
                self.range_matrix[row2][col1 - 1]
        if col1 == 0:
            return self.range_matrix[row2][col2] - \
                self.range_matrix[row1 - 1][col2]
        return self.range_matrix[row2][col2] + \
            self.range_matrix[row1 - 1][col1 - 1] - \
            self.range_matrix[row1 - 1][col2] - \
            self.range_matrix[row2][col1 - 1]


class NumMatrix2(object):
    def __init__(self, matrix):
        self.bit = BinaryIndexedTree2D(matrix)

    def update(self, row, col, val):
        self.bit.update(row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        return self.bit.sum(row2, col2) - self.bit.sum(row1 - 1, col2) - \
            self.bit.sum(row2, col1 - 1) + self.bit.sum(row1 - 1, col1 - 1)


def test_range_sum_query():
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(2, 1, 4, 3) == 8
    obj.update(3, 2, 2)
    assert obj.sumRegion(2, 1, 4, 3) == 10

    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    obj2 = NumMatrix2(matrix)
    assert obj2.sumRegion(2, 1, 4, 3) == 8
    obj2.update(3, 2, 2)
    assert obj2.sumRegion(2, 1, 4, 3) == 10

    matrix = [[1, 2]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 1
    assert obj.sumRegion(0, 1, 0, 1) == 2
    assert obj.sumRegion(0, 0, 0, 1) == 3
    obj.update(0, 0, 3)
    obj.update(0, 1, 5)
    assert obj.sumRegion(0, 0, 0, 1) == 8

    matrix = [[1, 2]]
    obj2 = NumMatrix2(matrix)
    assert obj2.sumRegion(0, 0, 0, 0) == 1
    assert obj2.sumRegion(0, 1, 0, 1) == 2
    assert obj2.sumRegion(0, 0, 0, 1) == 3
    obj2.update(0, 0, 3)
    obj2.update(0, 1, 5)
    assert obj2.sumRegion(0, 0, 0, 1) == 8


test_range_sum_query()
