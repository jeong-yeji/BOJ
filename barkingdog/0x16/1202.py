import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()
answer = 0
hq = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(hq, -heapq.heappop(jewels)[1])
    if hq:
        answer -= heapq.heappop(hq)
print(answer)
