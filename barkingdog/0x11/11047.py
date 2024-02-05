n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
answer = 0
for i in range(n - 1, -1, -1):
    d, m = divmod(k, a[i])
    if d > 0:
        k = m
        answer += d
print(answer)
