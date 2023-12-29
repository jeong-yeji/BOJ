import sys

input = lambda: sys.stdin.readline().strip()
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3], [0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

res, cctvs = [], []
for i in range(n):
    for j in range(m):
        if board[i][j] == 5:
            for dx, dy in delta:
                x, y = i, j
                while True:
                    x += dx
                    y += dy
                    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == 6:
                        break
                    if board[x][y] == 0:
                        board[x][y] = -1
        elif 0 < board[i][j] < 5:
            cctvs.append([i, j])


def execute(states, positions):
    for (i, j), position in positions:
        for d in directions[states[i][j]][position]:
            x, y = i, j
            dx, dy = delta[d]
            while True:
                x += dx
                y += dy
                if x < 0 or x >= n or y < 0 or y >= m or states[x][y] == 6:
                    break
                if states[x][y] == 0:
                    states[x][y] = -1
    res.append(sum(1 for r in states for c in r if c == 0))


# for product in product([0, 1, 2, 3], repeat=len(cctvs)):
#     execute([row[:] for row in board], list(zip(cctvs, product)))


def dfs(depth, cur):
    if depth == len(cctvs):
        execute([row[:] for row in board], list(zip(cctvs, cur)))
        return

    for i in range(2 if board[cctvs[depth][0]][cctvs[depth][1]] == 2 else 4):
        dfs(depth + 1, cur + [i])


dfs(0, [])
print(min(res))
