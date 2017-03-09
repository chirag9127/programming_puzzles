"""
Implement a deep iterator
"""
import collections


def test_deep_iterator():
    vector = [1, [2, 3], [], [4, [5, 6]], []]

    di = DeepIterator(vector)
    """
    assert di.has_next()
    assert di.next() == 1

    assert di.has_next()
    """

    for i in range(6):
        print (di.next())


class DeepIterator(object):

    def __init__(self, vector):
        self.flattened = []
        for i in self.__flatten(vector):
            self.flattened.append(i)

        self.item = 0

    def __flatten(self, vector):
        for el in vector:
            if isinstance(el, collections.Iterable):
                yield from self.__flatten(el)
            else:
                yield el

    def has_next(self):
        if self.item < len(self.flattened):
            return True
        return False

    def next(self):
        result = self.flattened[self.item]
        self.item += 1
        return result


class DeepIterator2(object):

    def __init__(self, vector):
        self.vector = vector
        self.inner = 0
        self.outer = 0
        self.non_none_inner = 0

    def has_next(self):
        if self.inner >= len(self.vector):
            return False
        inner_list = self.vector[self.inner]
        if not inner_list:
            self.inner += 1
            return self.has_next()
        if self.outer >= len(inner_list):
            self.outer = 0
            self.inner += 1
            return self.has_next()
        return True

    def next(self):
        if self.has_next():
            val = self.vector[self.inner][self.outer]
            self.outer += 1
            return val
        else:
            raise StopIteration

    def remove(self):
        rem_inner = self.inner
        rem_outer = self.outer
        if self.outer == 0:
            rem_inner = self.non_none_inner
        if rem_inner < len(self.vector):
            if rem_outer < len(self.vector[rem_inner]):
                del self.vector[rem_inner][rem_outer]
                self.outer = rem_outer
                self.inner = rem_inner
            else:
                self.outer = 0
                self.inner += 1


def test_deep_iterator_2():
    data = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8]]
    di2 = DeepIterator2(data)
    i = 0
    while i < 7:
        print (di2.next())
        di2.remove()
        print(di2.vector)
        i += 1


test_deep_iterator_2()
