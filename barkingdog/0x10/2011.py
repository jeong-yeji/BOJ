def sol1(n):
    if n[0] == 0:
        return 0

    dp = [0] * (len(n) + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, len(n) + 1):
        if n[i - 1]:
            dp[i] = dp[i - 1]
            if 10 <= n[i - 2] * 10 + n[i - 1] <= 26:
                dp[i] += dp[i - 2]
        else:
            if n[i - 2] == 1 or n[i - 2] == 2:
                dp[i] = dp[i - 2]
            else:
                return 0

    return dp[-1] % 1000000


def sol2(n):
    if n[0] == 0:
        return 0

    dp = [0] * (len(n) + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, len(n) + 1):
        if n[i - 1]:
            dp[i] += dp[i - 1]
        if 10 <= n[i - 2] * 10 + n[i - 1] <= 26:
            dp[i] += dp[i - 2]

    return dp[-1] % 1000000


if __name__ == "__main__":
    # print(sol1(list(map(int, input()))))
    print(sol2(list(map(int, input()))))
