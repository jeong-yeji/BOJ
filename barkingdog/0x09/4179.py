import sys
from collections import deque

input = sys.stdin.readline


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

fire = [[1_000_001] * c for _ in range(r)]
jihoon = [[1_000_001] * c for _ in range(r)]
fq = deque()
jhq = deque()
res = -1
for i in range(r):
    for j in range(c):
        if board[i][j] == "F":
            fire[i][j] = 0
            fq.append(Point(i, j))
        elif board[i][j] == "J":
            jihoon[i][j] = 0
            jhq.append(Point(i, j))
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                res = 0

while fq:
    cur = fq.popleft()

    for d in range(4):
        nx = cur.x + dx[d]
        ny = cur.y + dy[d]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if fire[nx][ny] != 1_000_001 or board[nx][ny] == "#":
            continue

        fire[nx][ny] = fire[cur.x][cur.y] + 1
        fq.append(Point(nx, ny))

while jhq and res == -1:
    cur = jhq.popleft()
    time = jihoon[cur.x][cur.y] + 1

    for d in range(4):
        nx = cur.x + dx[d]
        ny = cur.y + dy[d]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if board[nx][ny] == "#":
            continue

        if fire[nx][ny] <= time:
            continue

        if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
            res = time
            break

        if jihoon[nx][ny] == 1_000_001:
            jihoon[nx][ny] = time
            jhq.append(Point(nx, ny))

print(res + 1 if res != -1 else "IMPOSSIBLE")
