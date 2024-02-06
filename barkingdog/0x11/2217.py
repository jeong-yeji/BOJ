n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
res = 0
for i in range(n):
    res = max(res, rope[i] * (i + 1))
print(res)
