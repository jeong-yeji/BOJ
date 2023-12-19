def recur(i, j, n):
    cur = board[i][j]
    for x in range(i, i + n):
        for y in range(j, j + n):
            if cur != board[x][y]:
                for k in range(0, n, n // 3):
                    for l in range(0, n, n // 3):
                        recur(i + k, j + l, n // 3)
                return
    res[cur] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = [0] * 3
recur(0, 0, n)
print(res[-1])
print(res[0])
print(res[1])
