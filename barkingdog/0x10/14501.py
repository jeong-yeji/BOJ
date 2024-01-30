def bottom_up(n, arr):
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i + arr[i][0], n + 1):
            dp[j] = max(dp[j], dp[i] + arr[i][1])
    return dp[-1]


def top_down(n, arr):
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if i + arr[i][0] > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])
    return dp[0]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(bottom_up(n, arr))
    print(top_down(n, arr))
