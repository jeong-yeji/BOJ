import sys


def is_square(i, j):
    return board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]


input = lambda: sys.stdin.readline().strip()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[0] * 101 for _ in range(101)]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())

    directions = [d]
    for c in range(g):
        for i in range((1 << c) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    board[y][x] = 1
    for direction in directions:
        x += dx[direction]
        y += dy[direction]
        board[y][x] = 1

print(sum(is_square(i, j) for i in range(100) for j in range(100)))
