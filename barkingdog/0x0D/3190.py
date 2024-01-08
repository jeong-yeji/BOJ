import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    ax, ay = map(int, input().split())
    board[ax][ay] = 2

move = deque([input().split() for _ in range(int(input()))])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d, time = 1, 1, 0, 0
board[x][y] = 1
snake = deque([(x, y)])

while True:
    time += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if nx <= 0 or nx > n or ny <= 0 or ny > n or board[nx][ny] == 1:
        break

    if board[nx][ny] == 0:
        px, py = snake.popleft()
        board[px][py] = 0

    snake.append((nx, ny))
    board[nx][ny] = 1
    x, y = nx, ny

    if move and time == int(move[0][0]):
        _, c = move.popleft()
        if c == "L":
            d = (d - 1) % 4
        elif c == "D":
            d = (d + 1) % 4

print(time)
