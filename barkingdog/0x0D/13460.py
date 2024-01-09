import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = -1

red_x, red_y, blue_x, blue_y = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            red_x, red_y = i, j
        elif board[i][j] == "B":
            blue_x, blue_y = i, j

queue = deque([(red_x, red_y, blue_x, blue_y, 1)])
visited[red_x][red_y][blue_x][blue_y] = True

while queue:
    rx, ry, bx, by, k = queue.popleft()
    if answer > 0 or k > 10:
        break

    for dx, dy in delta:
        nrx, nry, nbx, nby = rx, ry, bx, by
        red, blue = 0, 0
        hole_in = False

        while True:
            if board[nbx + dx][nby + dy] == "#":
                break

            if board[nbx + dx][nby + dy] == "O":
                hole_in = True
                break

            blue += 1
            nbx += dx
            nby += dy

        if hole_in:
            continue

        while True:
            if board[nrx + dx][nry + dy] == "#":
                break

            if board[nrx + dx][nry + dy] == "O":
                answer = k
                break

            red += 1
            nrx += dx
            nry += dy

        if nrx == nbx and nry == nby:
            if red > blue:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy

        if not visited[nrx][nry][nbx][nby]:
            queue.append((nrx, nry, nbx, nby, k + 1))
            visited[nrx][nry][nbx][nby] = True

print(answer)
