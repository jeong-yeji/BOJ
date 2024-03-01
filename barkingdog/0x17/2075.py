import heapq
import sys

input = sys.stdin.readline
h = []
n = int(input())
for _ in range(n):
    for i in map(int, input().split()):
        if len(h) < n:
            heapq.heappush(h, i)
        elif i > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, i)
print(h[0])
