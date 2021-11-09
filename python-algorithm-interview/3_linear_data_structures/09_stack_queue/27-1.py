# merge-k-sorted-lists

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        root = res = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                # 동일한 값을 넣을 수 없으므로 추가 인자로 연결 리스트의 순서를 같이 삽입함
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            res.next = node[2]

            res = res.next
            if res.next:
                heapq.heappush(heap, (res.next.val, idx, res.next))

        return root.next


# PriorityQueue vs heapq
# 둘은 사실상 동일함
# PriorityQueue : Thread-Safe 보장
# heapq : Thread-Safe 보장하지 않음
# 멀티 스레드로 구현하지 않는다면 굳이 PriorityQueue 사용하지 않아도 됨
