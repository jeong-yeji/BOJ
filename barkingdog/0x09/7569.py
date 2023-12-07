import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

tomatoes = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tomatoes.append((i, j, k))

dx = [0, 0, 0, 0, 1, -1]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 1, 0, -1, 0, 0]

while tomatoes:
    x, y, z = tomatoes.popleft()

    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]

        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
            continue

        if box[nx][ny][nz] != 0:
            continue

        box[nx][ny][nz] = box[x][y][z] + 1
        tomatoes.append((nx, ny, nz))

flat = sum(sum(box, []), [])
print(-1 if 0 in flat else max(flat) - 1)
