def recur(i, j, n):
    if n == 1:
        print(board[i][j], end="")
        return

    cur = board[i][j]
    for x in range(i, i + n):
        for y in range(j, j + n):
            if cur != board[x][y]:
                print("(", end="")
                recur(i, j, n // 2)
                recur(i, j + n // 2, n // 2)
                recur(i + n // 2, j, n // 2)
                recur(i + n // 2, j + n // 2, n // 2)
                print(")", end="")
                return
    print(cur, end="")


n = int(input())
board = [list(input()) for _ in range(n)]
recur(0, 0, n)
