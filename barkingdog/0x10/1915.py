n, m = map(int, input().split())
square = [list(map(int, list(input()))) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if i and j and square[i][j]:
            square[i][j] += min(square[i - 1][j], square[i][j - 1], square[i - 1][j - 1])
        if square[i][j] > answer:
            answer = square[i][j]
print(answer * answer)
