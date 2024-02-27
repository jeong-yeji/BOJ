import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    minh, maxh, valid = [], [], [True] * 1_000_001
    for i in range(int(input())):
        op, n = input().split()
        n = int(n)

        if op == "I":
            heapq.heappush(minh, (n, i))
            heapq.heappush(maxh, (-n, i))
        else:
            if n == 1 and maxh:
                valid[heapq.heappop(maxh)[1]] = False
            elif n == -1 and minh:
                valid[heapq.heappop(minh)[1]] = False

        while maxh and not valid[maxh[0][1]]:
            heapq.heappop(maxh)
        while minh and not valid[minh[0][1]]:
            heapq.heappop(minh)

    if maxh and minh:
        print(-maxh[0][0], minh[0][0])
    else:
        print("EMPTY")
