import sys

input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
soil = [[5] * n for _ in range(n)]
trees = [[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] = 1

delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                dead_soil = 0
                tree_ij = {}
                no_soil = False
                for age in sorted(trees[i][j].keys()):
                    total_tree = trees[i][j][age]
                    if no_soil:
                        dead_soil += total_tree * (age // 2)
                    elif soil[i][j] >= total_tree * age:
                        soil[i][j] -= total_tree * age
                        tree_ij[age + 1] = total_tree
                    else:
                        no_soil = True
                        alive, dead = divmod(soil[i][j], age)
                        dead_soil += (total_tree - alive) * (age // 2)
                        if alive > 0:
                            soil[i][j] = dead
                            tree_ij[age + 1] = alive
                trees[i][j] = tree_ij
                soil[i][j] += dead_soil

    for i in range(n):
        for j in range(n):
            new_tree = 0
            for age in trees[i][j].keys():
                if age % 5 == 0:
                    new_tree += trees[i][j][age]
            if new_tree:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if 1 in trees[ni][nj]:
                            trees[ni][nj][1] += new_tree
                        else:
                            trees[ni][nj][1] = new_tree
            soil[i][j] += arr[i][j]

print(sum(sum(sum(col.values()) for col in row) for row in trees))
