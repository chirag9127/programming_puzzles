"""
Class for binary indexed tree
"""


class BinaryIndexedTree(object):

    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.bit = [0] * (self.length + 1)
        for i, val in enumerate(array):
            self.update(i, val)

    def update(self, pos, val):
        index = pos + 1

        while index <= self.length:
            self.bit[index] += val
            print index, self.bit
            index += index & (- index)

    def get_sum(self, pos):
        index = pos + 1
        res = 0
        while index > 0:
            res += self.bit[index]
            print index, res
            index -= index & (- index)
        return res


class BinaryIndexedTree2D(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.row_len = len(self.matrix)
        self.col_len = len(self.matrix[0])
        self.bit = [[0 for j in xrange(len(self.matrix[0]) + 1)]
                    for i in xrange(len(self.matrix) + 1)]
        for row in xrange(1, len(self.bit)):
            for col in xrange(1, len(self.bit[0])):
                for i in xrange(row + 1 - (row & -row), row + 1):
                    for j in xrange(col + 1 - (col & -col), col + 1):
                        self.bit[row][col] += self.matrix[i - 1][j - 1]

    def update(self, row, col, val):
        i = row + 1
        while i <= self.row_len:
            j = col + 1
            while j <= self.col_len:
                self.bit[i][j] += val - self.matrix[row][col]
                j += j & (-j)
            i += i & (-i)
        self.matrix[row][col] = val

    def sum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.bit[i][j]
                j = j - (j & -j)
            i = i - (i & - i)
        return res
