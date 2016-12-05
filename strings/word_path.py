"""
This program takes a starting word and ending word and creates a path from the
starting word to the ending word using the words in the dictionary.
"""


def test_word_path():
    dictionary = {'bat', 'rat', 'cat', 'cut', 'cup', 'hut', 'but',
                  'hub', 'pub', 'hum', 'hul', 'hal', 'put', 'cub'}
    result = word_path('cat', 'pub', dictionary)
    assert result in [['cat', 'cut', 'cub', 'pub'],
                      ['cat', 'cut', 'put', 'pub']]


class Node(object):

    def __init__(self, string):
        self.string = string
        self.adjacent_nodes = set()
        nodes[self.string] = self

nodes = {}


def get_adjacent_words(word, dictionary):
    for w in dictionary:
        if len(w) != len(word):
            continue
        num_different = 0
        for char1, char2 in zip(w, word):
            if char1 != char2:
                num_different += 1
        if num_different == 1:
            yield w


def create_graph(node, dictionary):
    for word in get_adjacent_words(node.string, dictionary):
        new_word = False
        if word in nodes:
            new_node = nodes[word]
        else:
            new_word = True
            new_node = Node(word)
        node.adjacent_nodes.add(new_node)
        if new_word:
            create_graph(new_node, dictionary)


def word_path(start, end, dictionary):
    root = Node(start)
    create_graph(root, dictionary)

    # Do BFS to get from start to end
    queue = [[root]]
    traversed_nodes = set()
    while len(queue) != 0:
        path = queue.pop(0)
        item = path[-1]
        if isinstance(item, Node) and item.string == end:
            path_str = [node.string for node in path]
            return path_str
        for adj_node in item.adjacent_nodes:
            if adj_node.string in traversed_nodes:
                continue
            traversed_nodes.add(adj_node.string)
            new_path = list(path)
            new_path.append(adj_node)
            queue.append(new_path)
