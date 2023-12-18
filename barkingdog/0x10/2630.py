def recur(i, j, n):
    cur = board[i][j]
    for x in range(i, i + n):
        for y in range(j, j + n):
            if cur != board[x][y]:
                recur(i, j, n // 2)
                recur(i, j + n // 2, n // 2)
                recur(i + n // 2, j, n // 2)
                recur(i + n // 2, j + n // 2, n // 2)
                return
    res[cur] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0]
recur(0, 0, n)
print("\n".join(map(str, res)))
