n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
x, y = lines[0][0], lines[0][1]
answer = 0
for i in range(1, n):
    s, e = lines[i][0], lines[i][1]
    if s > y:
        answer += y - x
        x, y = s, e
    elif x <= s <= y < e:
        y = e
print(answer + (y - x))
