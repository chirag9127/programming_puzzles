"""
Merge k sorted lists
"""
import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(lists):
    node_dict = {}
    result = []
    heap = []
    for list_node in lists:
        node_dict[list_node.val] = list_node
        heapq.heappush(heap, list_node.val)
    while len(heap) > 0:
        item = heapq.heappop(heap)
        result.append(item)
        next_item = node_dict[item].next
        if next_item:
            node_dict[next_item.val] = next_item
            heapq.heappush(heap, next_item.val)
    return result


def test_merge():
    l0 = ListNode(2)
    l0.next = ListNode(4)

    l1 = ListNode(1)
    l1.next = ListNode(5)

    l2 = ListNode(3)
    l2.next = ListNode(6)

    assert merge([l0, l1, l2]) == [1, 2, 3, 4, 5, 6]

    l3 = ListNode(1)
    assert merge([l3]) == [1]
