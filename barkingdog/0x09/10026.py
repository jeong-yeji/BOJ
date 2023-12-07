import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())
board = [input() for _ in range(n)]


def bfs():
    global n, dx, dy, board

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    vis = [[0] * n for _ in range(n)]
    q = deque()
    res = 0

    for i in range(n):
        for j in range(n):
            if vis[i][j]:
                continue

            res += 1
            q.append((i, j))
            vis[i][j] = 1

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if vis[nx][ny] or board[nx][ny] != board[x][y]:
                        continue

                    q.append((nx, ny))
                    vis[nx][ny] = 1

    return res


a = bfs()
board = [row.replace("R", "G") for row in board]
b = bfs()
print(a, b)
