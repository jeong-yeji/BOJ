import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    board = [[0] * m for _ in range(n)]
    for c in range(k):
        j, i = map(int, input().split())
        board[i][j] = 1

    queue = deque()
    res = 0

    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                continue

            queue.append((i, j))
            res += 1

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if not board[nx][ny]:
                        continue

                    board[nx][ny] = 0
                    queue.append((nx, ny))

    print(res)
