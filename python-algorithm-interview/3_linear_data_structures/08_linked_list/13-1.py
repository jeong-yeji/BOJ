# palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# linked list -> deque

from collections import deque

# pop(0)의 실행 속도 개선을 위해 deque 이용
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return True

        palindrome = deque()
        node = head
        while node is not None:
            palindrome.append(node.val)
            node = node.next

        while len(palindrome) > 1:
            if palindrome.popleft() != palindrome.pop():
                return False

        return True
