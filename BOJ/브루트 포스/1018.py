# 체스판 다시 칠하기
n, m = map(int, input().split())
chess = []
res = []

for _ in range(n):
    chess.append(input())

for row in range(n - 7):
    for column in range(m - 7):
        startW = 0
        startB = 0
        for i in range(row, row + 8):
            for j in range(column, column + 8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != "W":
                        startW += 1
                    if chess[i][j] != "B":
                        startB += 1
                else:
                    if chess[i][j] != "B":
                        startW += 1
                    if chess[i][j] != "W":
                        startB += 1
        res.append(startW)
        res.append(startB)

print(min(res))
