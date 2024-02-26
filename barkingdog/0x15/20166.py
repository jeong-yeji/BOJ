import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().strip()

n, m, k = list(map(int, input().split()))
info = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, - 1, 1, -1]
dic = defaultdict(int)

for i in range(n):
    for j in range(m):
        queue = deque([(i, j, info[i][j])])
        while queue:
            x, y, cur = queue.popleft()
            dic[cur] += 1

            if len(cur) >= 5:
                continue

            for d in range(8):
                nx = (x + dx[d] + n) % n
                ny = (y + dy[d] + m) % m
                queue.append((nx, ny, cur + info[nx][ny]))

for _ in range(k):
    print(dic[input()])
