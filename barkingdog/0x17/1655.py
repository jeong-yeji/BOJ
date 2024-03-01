import heapq
import sys

input = sys.stdin.readline
h1, h2 = [], []
for i in range(int(input())):
    num = int(input())
    if len(h1) == len(h2):
        heapq.heappush(h1, -num)
    else:
        heapq.heappush(h2, num)

    if h2 and h2[0] < -h1[0]:
        a = heapq.heappop(h1)
        b = heapq.heappop(h2)
        heapq.heappush(h1, -b)
        heapq.heappush(h2, -a)

    print(-h1[0])
