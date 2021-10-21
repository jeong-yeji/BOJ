# palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# runner
class Solution:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = fast = head

        # runner 이용. reverse linked list
        while fast and fast.next:
            # 빠른 러너는 두 칸씩 이동
            fast = fast.next.next
            # 느린 러너는 한 칸씩 이동하면서 역순 연결 리스트 rev 생성
            rev, rev.next, slow = slow, rev, slow.next

        # 입력값이 홀수일 때 == fast가 아직 None이 아님
        # 중앙값은 팰린드롬에서 배제됨 => slow 한 칸 더 이동
        if fast:
            slow = slow.next

        # check palindrome
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        # 정상적으로 종료됨 == palindrome == slow, rev 모두 None

        return not rev  # not slow도 가능
