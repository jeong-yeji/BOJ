from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

vis = [[0] * m for _ in range(n)]
queue = deque()
cnt, width = 0, 0

for i in range(n):
    for j in range(m):
        if vis[i][j] or board[i][j] == 0:
            continue

        cnt += 1
        w = 1
        vis[i][j] = 1
        queue.append(Point(i, j))

        while queue:
            cur = queue.popleft()

            for d in range(4):
                nx = cur.x + dx[d]
                ny = cur.y + dy[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if vis[nx][ny] or board[nx][ny] == 0:
                    continue

                w += 1
                vis[nx][ny] = 1
                queue.append(Point(nx, ny))

        width = max(w, width)

print(cnt)
print(width)
