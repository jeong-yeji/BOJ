import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(int(input())):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]

    person = [[1_000_001] * w for _ in range(h)]
    fq = deque()
    pq = deque()
    res = -1
    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                fq.append((i, j))
                board[i][j] = 0
            elif board[i][j] == "@":
                pq.append((i, j))
                person[i][j] = 0
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    res = 0

    while fq:
        x, y = fq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if board[nx][ny] == "#" or type(board[nx][ny]) == int:
                continue

            board[nx][ny] = board[x][y] + 1
            fq.append((nx, ny))

    while pq and res == -1:
        x, y = pq.popleft()
        time = person[x][y] + 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if board[nx][ny] == "#":
                continue

            if type(board[nx][ny]) == int and board[nx][ny] <= time:
                continue

            if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                res = time
                break

            if person[nx][ny] == 1_000_001:
                pq.append((nx, ny))
                person[nx][ny] = time

    print("IMPOSSIBLE" if res == -1 else res + 1)
