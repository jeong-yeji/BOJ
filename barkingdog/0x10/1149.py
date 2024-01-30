import sys

input = lambda: sys.stdin.readline().strip()


def sol1(n):
    houses = [[0, 0, 0] for _ in range(1001)]
    for i in range(1, n + 1):
        houses[i] = list(map(int, input().split()))

    dp = [[0, 0, 0] for _ in range(1001)]
    dp[1] = houses[1]
    for i in range(2, n + 1):
        dp[i][0] = houses[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = houses[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = houses[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    return min(dp[n])


def sol2(n):
    dp = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    return min(dp[-1])


if __name__ == "__main__":
    n = int(input())
    print(sol1(n))
    print(sol2(n))
