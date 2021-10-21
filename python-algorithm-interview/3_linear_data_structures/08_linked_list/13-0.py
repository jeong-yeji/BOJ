# palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# linked list -> list
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return True

        # palindrome: List = []
        palindrome = []
        node = head
        while node:
            palindrome.append(node.val)
            node = node.next

        while len(palindrome) > 1:
            if palindrome.pop(0) != palindrome.pop():
                return False

        return True
