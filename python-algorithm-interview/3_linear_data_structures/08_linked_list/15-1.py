# reverse-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 재귀 구조
class Solution:
    def reverseList(self, head):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
