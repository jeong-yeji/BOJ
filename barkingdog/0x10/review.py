import itertools
import sys

input = lambda: sys.stdin.readline().strip()


def q1463():
    dp = {1: 0, 2: 1}

    def recur(i):
        if i not in dp:
            dp[i] = 1 + min(recur(i // 3) + i % 3, recur(i // 2) + i % 2)
        return dp[i]

    print(recur(int(input())))


def q9095():
    dp = [0, 1, 2, 4]
    for i in range(4, 11):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    for _ in range(int(input())):
        print(dp[int(input())])


def q2579():
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    if n < 3:
        print(sum(stairs))
        exit()
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]
    for i in range(3, n):
        dp[i] = stairs[i] + max(dp[i - 2], dp[i - 3] + stairs[i - 1])
    print(dp[-1])


def q1149():
    n = int(input())
    houses = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])
        houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])
        houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])
    print(min(houses[-1]))


def q11726():
    n = int(input())
    dp = [0, 1, 2]
    for _ in range(n - 2):
        dp.append((dp[-1] + dp[-2]) % 10007)
    print(dp[n])


def q11659():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    acc = [0] + list(itertools.accumulate(numbers))
    for _ in range(m):
        s, e = map(int, input().split())
        print(acc[e] - acc[s - 1])


def q12852():
    dp = {1: 0, 2: 1}

    def recur(i):
        if i not in dp:
            dp[i] = 1 + min(recur(i // 3) + i % 3, recur(i // 2) + i % 2)
        return dp[i]

    def find_path(a, b):
        while a % b:
            a -= 1
            print(a, end=' ')
        a //= b
        print(a, end=' ')
        return a

    n = int(input())
    print(recur(n), n, sep='\n', end=' ')
    while n > 1:
        if dp[n] == dp[n // 2] + n % 2 + 1:
            n = find_path(n, 2)
        else:
            n = find_path(n, 3)


def q1003():
    for _ in range(int(input())):
        z, o = 1, 0
        for _ in range(int(input())):
            z, o = o, z + o
        print(z, o)


def q1932():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                tri[i][j] += tri[i - 1][j]
            elif j == i:
                tri[i][j] += tri[i - 1][j - 1]
            else:
                tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])
    print(max(tri[-1]))


def q11727():
    n = int(input())
    dp = [0, 1, 3]
    for _ in range(n - 2):
        dp.append(dp[-1] + dp[-2] * 2)
    print(dp[n] % 10007)


def q2193():
    n = int(input())
    z, o = 0, 1
    for _ in range(n - 1):
        z, o = z + o, z
    print(z + o)


def q1912():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = numbers[:]
    for i in range(1, n):
        if dp[i - 1] > 0:
            dp[i] += dp[i - 1]
    print(max(dp))


def q11055():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * 1001
    for i, v in enumerate(a):
        dp[v] = v + max(dp[:v])
    print(max(dp))


def q11053():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    print(max(dp))


def q9461():
    dp = [1] * 101
    for i in range(4, 101):
        dp[i] = dp[i - 2] + dp[i - 3]
    for _ in range(int(input())):
        print(dp[int(input())])


def q14501():
    n = int(input())
    interviews = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i + interviews[i][0], n + 1):
            if dp[i] + interviews[i][1] > dp[j]:
                dp[j] = dp[i] + interviews[i][1]
    print(dp[n])


def q15486():
    n = int(input())
    a = [map(int, input().split()) for _ in range(n)]
    dp = [0] * (n + 1)
    for i, (t, p) in enumerate(a):
        if dp[i] > dp[i + 1]:
            dp[i + 1] = dp[i]
        if i + t <= n and dp[i] + p > dp[i + t]:
            dp[i + t] = dp[i] + p
    print(dp[n])


def q10844():
    n = int(input())
    dp = [[0] * 10 for _ in range(n)]
    dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    print(sum(dp[n - 1]) % 1_000_000_000)


def q10942():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n and numbers[i] == numbers[i + 1]:
            dp[i][i + 1] = 1
    for offset in range(2, n):
        for i in range(n - offset):
            if numbers[i] == numbers[i + offset]:
                dp[i][i + offset] = dp[i + 1][i + offset - 1]
    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])


def q9655():
    print(['CY', 'SK'][int(input()) % 2])


def q1699():
    n = int(input())
    dp = list(range(n + 1))
    for i in range(1, n + 1):
        for j in range(1, int(i ** 0.5) + 1):
            sq = j * j
            if sq <= i and dp[i] > dp[i - sq] + 1:
                dp[i] = dp[i - sq] + 1
    print(dp[n])


def q2011():
    code = list(map(int, input()))
    if code[0] == 0:
        print(0)
        return

    dp = [0] * (len(code) + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, len(code) + 1):
        if code[i - 1]:
            dp[i] += dp[i - 1]
        if 10 <= code[i - 2] * 10 + code[i - 1] < 27:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)


def q1915():
    n, m = map(int, input().split())
    square = [list(map(int, input())) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if square[i][j]:
                square[i][j] += min(square[i - 1][j], square[i][j - 1], square[i - 1][j - 1])
    print(max(sum(square, [])) ** 2)


def q9084():
    for _ in range(int(input())):
        n = int(input())
        coins = list(map(int, input().split()))
        m = int(input())
        dp = [0] * (m + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, m + 1):
                dp[i] += dp[i - coin]
        print(dp[m])


def q9251():
    A, B = input(), input()
    dp = [[0] * 1001 for _ in range(1001)]
    for i, a in enumerate(A, start=1):
        for j, b in enumerate(B, start=1):
            if a == b:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[len(A)][len(B)])


def sol():
    q9251()


if __name__ == "__main__":
    sol()
