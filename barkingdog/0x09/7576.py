import sys
from collections import deque

input = sys.stdin.readline


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dates = [[1_000_001] * m for _ in range(n)]
tomatoes = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] != 0:
            dates[i][j] = 0
            cnt += 1
            if box[i][j] == 1:
                tomatoes.append(Point(i, j))

if cnt == m * n:
    print(0)
else:
    while tomatoes:
        cur = tomatoes.popleft()

        for d in range(4):
            nx = cur.x + dx[d]
            ny = cur.y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if dates[nx][ny] != 1_000_001 or box[nx][ny] == -1:
                continue

            dates[nx][ny] = dates[cur.x][cur.y] + 1
            tomatoes.append(Point(nx, ny))

    if 1_000_001 in sum(dates, []):
        print(-1)
    else:
        print(max(map(max, dates)))
