import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
vis = [[[0, 0] for _ in range(m)] for _ in range(n)]
vis[0][0][0] = 1
vis[0][0][1] = 1
q.append((0, 0, 0, 0))
res = 1_000_001

while q:
    x, y, dist, broken = q.popleft()
    if x == n - 1 and y == m - 1:
        res = dist + 1
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if vis[nx][ny][broken]:
            continue

        if not board[nx][ny]:
            vis[nx][ny][broken] = 1
            q.append((nx, ny, dist + 1, broken))
        elif not broken:
            vis[nx][ny][broken] = 1
            q.append((nx, ny, dist + 1, 1))

print(-1 if res == 1_000_001 else res)
