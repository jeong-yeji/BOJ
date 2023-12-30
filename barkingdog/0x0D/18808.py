import sys


def put(r, c, sticker):
    global n, m
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            if is_available(i, j, r, c, sticker):
                mark(i, j, r, c, sticker)
                return True
    return False


def is_available(x, y, r, c, sticker):
    global n, m
    for i in range(r):
        for j in range(c):
            if sticker[i][j] and board[x + i][y + j]:
                return False
    return True


def mark(x, y, r, c, sticker):
    for i in range(r):
        for j in range(c):
            board[x + i][y + j] |= sticker[i][j]


input = lambda: sys.stdin.readline().strip()
n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for _ in range(4):
        if put(r, c, sticker):
            break
        r, c = c, r
        sticker = list(zip(*sticker[::-1]))

print(sum(sum(board, [])))
