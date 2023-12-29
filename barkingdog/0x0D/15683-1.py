import sys


def upd(x, y, dir):
    global n, m
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m or board2[x][y] == 6:
            return
        if board2[x][y] != 0:
            continue
        board2[x][y] = 7


input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
board1 = [list(map(int, input().split())) for _ in range(n)]

cctvs = [(i, j) for i in range(n) for j in range(m) if 0 < board1[i][j] < 6]
mn = sum(board1[i][j] == 0 for i in range(n) for j in range(m))

for tmp in range(1 << (2 * len(cctvs))):
    board2 = [row[:] for row in board1]
    brute = tmp
    for x, y in cctvs:
        brute, d = divmod(brute, 4)
        if board1[x][y] == 1:
            upd(x, y, d)
        elif board1[x][y] == 2:
            upd(x, y, d)
            upd(x, y, d + 2)
        elif board1[x][y] == 3:
            upd(x, y, d)
            upd(x, y, d + 1)
        elif board1[x][y] == 4:
            upd(x, y, d)
            upd(x, y, d + 1)
            upd(x, y, d + 2)
        elif board1[x][y] == 5:
            upd(x, y, d)
            upd(x, y, d + 1)
            upd(x, y, d + 2)
            upd(x, y, d + 3)
    mn = min(mn, sum(board2[i][j] == 0 for i in range(n) for j in range(m)))

print(mn)
