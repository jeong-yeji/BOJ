import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    cnt = [0] * (n + 1)

    for val in arr:
        cnt[val] += 1

    queue = deque()
    for i in range(1, n + 1):
        if cnt[i] == 0:
            queue.append(i)

    res = 0
    while queue:
        cur = queue.popleft()
        res += 1
        nxt = arr[cur]
        cnt[nxt] -= 1
        if cnt[nxt] == 0:
            queue.append(nxt)

    print(res)
