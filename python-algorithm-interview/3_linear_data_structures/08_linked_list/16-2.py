# add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# recursive full adder
class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and carry == 0:
            return None

        val1 = 0 if not l1 else l1.val
        val2 = 0 if not l2 else l2.val

        carry, val = divmod(val1 + val2 + carry, 10)
        res = ListNode(val)

        next1 = None if not l1 else l1.next
        next2 = None if not l2 else l2.next

        res.next = self.addTwoNumbers(next1, next2, carry)

        return res
