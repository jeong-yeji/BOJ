import heapq
import sys

input = sys.stdin.readline


def sol1(arr):
    heap = []
    for limit, ea in arr:
        heapq.heappush(heap, ea)
        if limit < len(heap):
            heapq.heappop(heap)
    return sum(heap)


def sol2(arr):
    heap = []
    cur = 1
    for limit, ea in arr:
        if cur <= limit:
            heapq.heappush(heap, ea)
            cur += 1
        elif heap[0] < ea:
            heapq.heappop(heap)
            heapq.heappush(heap, ea)
    return sum(heap)


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    print(sol1(arr))
    print(sol2(arr))
