# 분해합
n = int(input())
res = 0
for i in range(1, n):
    s = i + sum(list(map(int, str(i))))
    if s == n:
        res = i
        break
print(res)