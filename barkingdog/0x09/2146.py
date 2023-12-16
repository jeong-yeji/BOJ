import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

islands = []
cnt = 0
res = 100_001

queue = deque()
vis = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] and not vis[i][j]:
            queue.append((i, j))
            vis[i][j] = True
            island = [(i, j)]
            cnt += 1
            board[i][j] = cnt

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if vis[nx][ny] or not board[nx][ny]:
                        continue

                    queue.append((nx, ny))
                    island.append((nx, ny))
                    vis[nx][ny] = True
                    board[nx][ny] = cnt

            islands.append(island)


def calc(f, t):
    global res
    for x1, y1 in islands[f]:
        for x2, y2 in islands[t]:
            res = min(res, (abs(x2 - x1) + abs(y2 - y1) - 1))
            if res == 1:
                return


for i in range(cnt - 1):
    for j in range(i + 1, cnt):
        calc(i, j)
        if res == 1:
            break
    if res == 1:
        break

print(res)
