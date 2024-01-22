import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
nutrient = [[5] * n for _ in range(n)]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            dead = 0
            aged = deque()
            for age in trees[i][j]:
                if nutrient[i][j] >= age:
                    nutrient[i][j] -= age
                    aged.append(age + 1)
                else:
                    dead += age // 2
            nutrient[i][j] += dead
            trees[i][j] = aged

    new_trees = []
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += arr[i][j]
            for tree in trees[i][j]:
                if tree % 5 == 0:
                    for dx, dy in delta:
                        if 0 <= i + dx < n and 0 <= j + dy < n:
                            new_trees.append((i + dx, j + dy))
    for r, c in new_trees:
        trees[r][c].appendleft(1)

print(sum(sum(len(row) for row in matrix) for matrix in trees))
