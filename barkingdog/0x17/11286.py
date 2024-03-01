import heapq
import sys

input = sys.stdin.readline
absh = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(absh)[1] if absh else 0)
    else:
        heapq.heappush(absh, (abs(x), x))
