def sol1(n):
    dp = list(range(n + 1))
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            square = j * j
            if square > i:
                break
            if dp[i] > dp[i - square] + 1:
                dp[i] = dp[i - square] + 1
    return dp[n]


def is_square(n):
    return n == int(n ** 0.5) ** 2


def sol2(n):
    if is_square(n):
        return 1

    while n % 4 == 0:
        n //= 4

    if n % 8 == 7:
        return 4

    for i in range(1, int((n / 2) ** 0.5) + 1):
        if is_square(n - i * i):
            return 2

    return 3


if __name__ == "__main__":
    n = int(input())
    print(sol1(n))
    print(sol2(n))
