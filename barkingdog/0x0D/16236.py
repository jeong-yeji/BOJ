import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

fishes = []
si, sj = -1, -1
for i in range(n):
    for j in range(n):
        if 0 < board[i][j] < 7:
            fishes.append((i, j))
        elif board[i][j] == 9:
            si, sj = i, j
            board[i][j] = 0

delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
time, shark, ate = 0, 2, 0
while True:
    eatable = []
    distance = [[-1] * n for _ in range(n)]
    queue = deque([(si, sj)])
    distance[si][sj] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > shark or distance[nx][ny] != -1:
                continue
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))
            if 0 < board[nx][ny] < shark:
                eatable.append((nx, ny, distance[nx][ny]))

    if not eatable:
        print(time)
        break

    eatable.sort(key=lambda x: (x[2], x[0], x[1]))
    x, y, z = eatable[0]
    si, sj = x, y
    board[x][y] = 0
    ate += 1
    time += z

    if ate == shark:
        ate = 0
        shark += 1
