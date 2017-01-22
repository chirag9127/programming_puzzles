"""
Write a program to find the node at which the intersection of
two singly linked lists begins.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def find_intersection_squared(head1, head2):
    while head1:
        head2_copy = head2
        while head2_copy:
            if head2_copy.val == head1.val:
                return head2_copy
            head2_copy = head2_copy.next
        head1 = head1.next
    return None


def find_intersection_linear(head1, head2):
    len1 = 0
    len2 = 0
    head1_copy, head2_copy = head1, head2
    while head1_copy:
        len1 += 1
        head1_copy = head1_copy.next
    while head2_copy:
        len2 += 1
        head2_copy = head2_copy.next
    while len1 > len2:
        head1 = head1.next
        len1 -= 1
    while len2 > len1:
        head2 = head2.next
        len2 -= 1
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1


def test_find_intersection():
    h1 = ListNode(1)
    h12 = ListNode(2)
    h1.next = h12
    h13 = ListNode(3)
    h12.next = h13
    h14 = ListNode(4)
    h13.next = h14

    h2 = ListNode(5)
    h2.next = h13
    assert find_intersection_linear(h1, h2) == h13
