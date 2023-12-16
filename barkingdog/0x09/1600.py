import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

dx = [1, 0, -1, 0, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, 1, 0, -1, -1, 1, -2, 2, -2, 2, -1, 1]

vis = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
q = deque()

vis[0][0][0] = 1
q.append((0, 0, 0))


def bfs():
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1:
            return vis[x][y][z] - 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not can_pass(nx, ny, z):
                vis[nx][ny][z] = vis[x][y][z] + 1
                q.append((nx, ny, z))

        if z < k:
            for d in range(4, 12):
                nx = x + dx[d]
                ny = y + dy[d]
                if not can_pass(nx, ny, z + 1):
                    vis[nx][ny][z + 1] = vis[x][y][z] + 1
                    q.append((nx, ny, z + 1))

    return -1


def can_pass(nx, ny, z):
    return nx < 0 or nx >= h or ny < 0 or ny >= w or vis[nx][ny][z] or board[nx][ny]


print(bfs())
