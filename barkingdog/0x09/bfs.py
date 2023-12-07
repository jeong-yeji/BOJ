from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = 7, 10
board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
vis = [[False] * m for _ in range(n)]

queue = deque()

vis[0][0] = True
queue.append(Point(0, 0))

while queue:
    cur = queue.popleft()
    for d in range(4):
        nx = cur.x + dx[d]
        ny = cur.y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if vis[nx][ny] or board[nx][ny] != 1:
            continue

        vis[nx][ny] = True
        queue.append(Point(nx, ny))
