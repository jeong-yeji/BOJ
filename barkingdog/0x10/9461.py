dp = [1, 1, 1, 2, 2]
for i in range(5, 100):
    dp.append(dp[i - 5] + dp[i - 1])
for _ in range(int(input())):
    n = int(input())
    print(dp[n - 1])
