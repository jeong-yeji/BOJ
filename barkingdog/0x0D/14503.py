import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

board[r][c] = 2
answer = 1
while True:
    for _ in range(4):
        d = (d - 1) % 4
        nr = r + delta[d][0]
        nc = c + delta[d][1]

        if nr < 0 or nr >= n or nr < 0 or nc >= m or board[nr][nc] != 0:
            continue

        board[nr][nc] = 2
        answer += 1
        r, c = nr, nc
        break
    else:
        r, c = r - delta[d][0], c - delta[d][1]
        if board[r][c] == 1:
            print(answer)
            break
