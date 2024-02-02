import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    if i + 1 < n and numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1
for k in range(2, n):
    for i in range(n - k):
        if numbers[i] == numbers[i + k]:
            dp[i][i + k] = dp[i + 1][i + k - 1]

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
