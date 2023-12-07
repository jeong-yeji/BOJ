from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]

path = [[10001] * m for _ in range(n)]
queue = deque()

path[0][0] = 1
queue.append(Point(0, 0))

while queue:
    cur = queue.popleft()

    for d in range(4):
        nx = cur.x + dx[d]
        ny = cur.y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if path[nx][ny] != 10001 or board[nx][ny] == 0:
            continue

        path[nx][ny] = min(path[nx][ny], path[cur.x][cur.y] + 1)
        queue.append(Point(nx, ny))

print(path[n - 1][m - 1])
