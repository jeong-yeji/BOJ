# reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 반복 구조
class Solution:
    def reverseList(self, head):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
