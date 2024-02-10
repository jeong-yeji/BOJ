import math


def sol1(n, k):
    res = 1
    for i in range(1, n + 1):
        res *= i
    for i in range(1, k + 1):
        res //= i
    for i in range(1, n - k + 1):
        res //= i
    return res


def sol2(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(sol1(n, k))
    print(sol2(n, k))
