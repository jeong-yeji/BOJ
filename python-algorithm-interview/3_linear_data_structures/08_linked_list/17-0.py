# swap-nodes-in-pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            a = prev.next
            b = head.next
            c = head.next.next

            prev.next, b.next, a.next = b, a, c

            prev = a
            head = c

        return root.next
