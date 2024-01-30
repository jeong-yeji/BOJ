n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

if n < 3:
    print(sum(stairs))
else:
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, n + 1):
        dp[i] = stairs[i] + max(dp[i - 3] + stairs[i - 1], dp[i - 2])

    print(dp[n])
