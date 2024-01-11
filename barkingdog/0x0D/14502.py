import itertools
import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0

available, virus, walls = [], [], []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            walls.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
        else:
            available.append((i, j))

for combination in itertools.combinations(available, 3):
    arr = [b[:] for b in board]
    for x, y in combination:
        arr[x][y] = 1

    queue = deque()
    for x, y in virus:
        queue.append((x, y))

    cnt = n * m - len(virus) - len(walls) - 3
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = 2
                cnt -= 1

    answer = max(answer, cnt)

print(answer)
