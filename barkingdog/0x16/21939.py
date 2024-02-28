import heapq
import sys

input = sys.stdin.readline

minh, maxh, solved = [], [], {}
for _ in range(int(input())):
    p, l = map(int, input().split())
    heapq.heappush(minh, (l, p))
    heapq.heappush(maxh, (-l, -p))
    solved[p] = False

for _ in range(int(input())):
    op, *n = input().split()
    n = list(map(int, n))
    if op == "add":
        heapq.heappush(minh, (n[1], n[0]))
        heapq.heappush(maxh, (-n[1], -n[0]))
        solved[n[0]] = False
    elif op == "recommend":
        if n[0] == 1:
            print(-maxh[0][1])
        elif n[0] == -1:
            print(minh[0][1])
    elif op == "solved":
        solved[n[0]] = True

    while minh and solved[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and solved[-maxh[0][1]]:
        heapq.heappop(maxh)
