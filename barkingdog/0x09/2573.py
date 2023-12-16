import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] != 0:
            q.append((i, j))


def bfs():
    year = 0
    while q:
        year += 1

        for _ in range(len(q)):
            x, y = q.popleft()
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if board[nx][ny] == 0:
                    cnt += 1

            q.append((x, y, board[x][y] - cnt))

        for _ in range(len(q)):
            x, y, res = q.popleft()
            if res > 0:
                q.append((x, y))
            else:
                res = 0
            board[x][y] = res

        if not q:
            return 0

        vis = [[0] * m for _ in range(n)]
        queue = deque()
        x, y = q[0]
        queue.append((x, y))
        vis[x][y] = 1
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if board[nx][ny] and not vis[nx][ny]:
                    queue.append((nx, ny))
                    vis[nx][ny] = 1

        for x, y in q:
            if board[x][y] and not vis[x][y]:
                return year

    return 0


print(bfs())
