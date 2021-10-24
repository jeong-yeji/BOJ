# add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 전가산기(Full Adder) 방식
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = node = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            node.next = ListNode(val)
            node = node.next

        return res.next
