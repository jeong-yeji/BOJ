import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n, l, r = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(i % 2, n, 2):
            if visited[i][j]:
                continue

            visited[i][j] = True
            queue = deque([(i, j)])
            country = [(i, j)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                        continue

                    if l <= abs(ground[x][y] - ground[nx][ny]) <= r:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        country.append((nx, ny))

            if len(country) > 1:
                flag = True
                divided = sum(ground[x][y] for x, y in country) // len(country)
                for x, y in country:
                    ground[x][y] = divided

    if not flag:
        break
    days += 1

print(days)
