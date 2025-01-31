# 78492kb, 580ms
def sol1(n):
    dp, pre = [0] * (n + 1), [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        pre[i] = i - 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            pre[i] = i // 2

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            pre[i] = i // 3

    print(dp[n])
    while True:
        print(n, end=" ")
        if n == 1:
            break
        n = pre[n]


d = {1: 0, 2: 1}


# 31120kb, 60ms
def sol2(n):
    print(s(n), n, sep='\n', end=' ')
    while n > 1:
        if d[n] == d[n // 2] + 1 + n % 2:
            if n % 2:
                n -= 1
                print(n, end=' ')
            n //= 2
            print(n, end=' ')
        else:
            while n % 3:
                n -= 1
                print(n, end=' ')
            n //= 3
            print(n, end=' ')


def s(n):
    if n in d:
        return d[n]
    t = 1 + min(s(n // 3) + n % 3, s(n // 2) + n % 2)
    d[n] = t
    return t


if __name__ == "__main__":
    n = int(input())
    # sol1(n)
    sol2(n)
