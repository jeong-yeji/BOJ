import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n, l, r = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
days = 0

queue = deque([(i, j) for i in range(n) for j in range(i % 2, n, 2)])
while queue:
    visited = [[False] * n for _ in range(n)]

    for _ in range(len(queue)):
        i, j = queue.popleft()
        if visited[i][j]:
            continue

        visited[i][j] = True
        population = ground[i][j]
        stack = [(i, j)]
        for x, y in stack:
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                    continue

                if l <= abs(ground[x][y] - ground[nx][ny]) <= r:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    population += ground[nx][ny]

        if len(stack) > 1:
            population //= len(stack)
            for x, y in stack:
                ground[x][y] = population
                queue.append((x, y))
    days += 1

print(days - 1)
