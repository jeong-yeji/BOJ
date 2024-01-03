import sys

input = lambda: sys.stdin.readline().strip()

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dice = [0] * 6
delta = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

for cmd in list(map(int, input().split())):
    nx = x + delta[cmd][0]
    ny = y + delta[cmd][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    if cmd == 1:  # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif cmd == 2:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif cmd == 3:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif cmd == 4:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5], board[x][y] = board[x][y], 0

    print(dice[0])
