"""
Design and implement a data structure for Least Recently Used (LRU) cache.
"""


class Node(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append_data(self, key, data):
        node = Node(key, data)
        self.append_node(node)
        return node

    def append_node(self, node):
        if self.tail:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def remove_node(self, node):
        if not node:
            return
        prev_node = node.prev_node
        next_node = node.next_node

        if not prev_node:
            self.head = next_node
            if self.head:
                self.head.prev_node = None

        if not next_node:
            self.tail = prev_node
            if self.tail:
                self.tail.next_node = None

        if next_node and prev_node:
            prev_node.next_node = next_node
            next_node.prev_node = prev_node

        node.next_node = None
        node.prev_node = None


class LRUCache(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.cache_index = {}
        self.cache = DoubleLinkedList()

    def put(self, key, data):
        node = self.cache_index.get(key)
        if node:
            self.cache.remove_node(node)
            node.data = data
            self.cache.append_node(node)
        else:
            if len(self.cache_index) >= self.max_size:
                self.__evict()
            node = self.cache.append_data(key, data)
            self.cache_index[key] = node

    def get(self, key):
        node = self.cache_index.get(key)
        if not node:
            return -1
        self.cache.remove_node(node)
        self.cache.append_node(node)
        return node.data

    def __evict(self):
        node = self.cache.head
        self.cache.remove_node(node)
        if node:
            del self.cache_index[node.key]


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
