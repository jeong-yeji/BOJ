# merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        # 작은 값이 l1에 오도록 함
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        # 다음 값이 엮이도록 재귀 호출
        if l1:  # l1이 None이면 마지막 노드 => 재귀가 끝남
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1
