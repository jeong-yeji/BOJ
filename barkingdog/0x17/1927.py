import heapq
import sys

input = sys.stdin.readline
minh = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(minh) if minh else 0)
    else:
        heapq.heappush(minh, x)
