import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(int(input())):
    l = int(input())
    board = [[-1] * l for _ in range(l)]

    cx, cy = map(int, input().split())
    q = deque([(cx, cy)])
    board[cx][cy] = 0

    tx, ty = map(int, input().split())

    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if board[nx][ny] != -1:
                continue

            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

        if board[tx][ty] > -1:
            break

    print(board[tx][ty])
