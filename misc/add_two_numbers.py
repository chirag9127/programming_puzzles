"""
You are given two non-empty linked lists representing
two non-negative integers.
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def add_numbers(l1, l2):
    carry = 0
    if not l1 and not l2:
        return None
    res = res_copy = ListNode(0)
    while l1 or l2 or carry > 0:
        curr = 0
        if l1:
            curr += l1.val
            l1 = l1.next
        if l2:
            curr += l2.val
            l2 = l2.next
        curr += carry
        curr_val = curr % 10
        carry = curr / 10
        res_copy.next = ListNode(curr_val)
        res_copy = res_copy.next
    return res.next


def test_add_numbers():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = add_numbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
    assert res.next.next.next is None
