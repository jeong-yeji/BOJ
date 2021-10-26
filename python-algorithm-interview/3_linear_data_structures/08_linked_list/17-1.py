# swap-nodes-in-pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 반복 구조로 스왑
    def iteration(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 이동
            head = head.next
            prev = prev.next.next

        return root.next

    # 재귀 구조로 스왑
    def recursive(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.recursive(p.next)
            p.next = head
            return p
        return head
