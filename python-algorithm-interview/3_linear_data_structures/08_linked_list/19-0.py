# reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        res = res[: left - 1] + res[left - 1 : right][::-1] + res[right:]

        root = node = ListNode()
        for i in res:
            node.next = ListNode(i)
            node = node.next

        return root.next
