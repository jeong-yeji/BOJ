# merge-k-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = head = ListNode()
        values = []

        for list in lists:
            while list:
                values.append(list.val)
                list = list.next
        values.sort()

        for value in values:
            head.next = ListNode(value)
            head = head.next

        return res.next
