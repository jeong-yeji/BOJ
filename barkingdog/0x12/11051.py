def sol1(n, k):
    dp = [[0] * 1001 for _ in range(1001)]
    for i in range(1, 1001):
        dp[i][0], dp[i][i] = 1, 1
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[n][k] % 10007


def sol2(n, k):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i][i] = 1
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[n][k] % 10007


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(sol1(n, k))
    print(sol2(n, k))
