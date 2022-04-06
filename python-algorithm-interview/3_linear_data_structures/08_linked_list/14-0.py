# merge-two-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        res = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next

        if l1:
            node.next = l1
        elif l2:
            node.next = l2

        return res.next
