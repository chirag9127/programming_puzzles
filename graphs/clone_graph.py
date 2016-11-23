"""
Given a graph, clone it (not provide a reference to the original graph)
"""


class Node:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


node_dict = {}


def copy_node(node, new_node):
    for neighbor in node.neighbors:
        traverse = False
        if neighbor.label in node_dict:
            neighbor_node = node_dict[neighbor.label]
        else:
            neighbor_node = Node(neighbor.label)
            node_dict[neighbor.label] = neighbor_node
            traverse = True
        new_node.neighbors.append(neighbor_node)
        print "Attaching {} to {}".format(neighbor_node.label, new_node.label)
        if traverse:
            copy_node(neighbor, neighbor_node)


def clone_graph(node):
    new_node = Node(node.label)
    node_dict[node.label] = new_node
    copy_node(node, new_node)
    return new_node


def test():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node0.neighbors.extend([node1])
    node1.neighbors.append(node2)
    node2.neighbors.append(node2)
    copy_node = clone_graph(node0)
