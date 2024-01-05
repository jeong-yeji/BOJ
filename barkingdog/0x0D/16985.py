import itertools
import sys
from collections import deque


def rotate(idx, times):
    origin = board[idx]
    for _ in range(times):
        origin = list(zip(*origin[::-1]))
    return origin


board = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)] for _ in range(5)]
r = [[rotate(i, t) for t in range(4)] for i in range(5)]

orders = list(itertools.permutations([0, 1, 2, 3, 4]))
rotations = list(itertools.product([0, 1, 2, 3], repeat=5))
cases = [list(zip(order, rotation)) for order in orders for rotation in rotations]

delta = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
answer = sys.maxsize

for case in cases:
    rotated = [r[i][d] for i, d in case]

    if rotated[0][0][0] == 0 or rotated[4][4][4] == 0:
        continue

    queue = deque([(0, 0, 0)])
    visited = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    while queue:
        x, y, z = queue.popleft()

        if x == 4 and y == 4 and z == 4:
            answer = min(answer, visited[4][4][4])
            break

        for dx, dy, dz in delta:
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5:
                continue

            if rotated[nx][ny][nz] == 0 or visited[nx][ny][nz] != sys.maxsize:
                continue

            queue.append((nx, ny, nz))
            visited[nx][ny][nz] = visited[x][y][z] + 1

    if answer == 12:
        break

print(-1 if answer == sys.maxsize else answer)
