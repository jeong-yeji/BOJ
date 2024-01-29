# 38932kb, 540ms
def sol1(n):
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
    return d[n]


d = {1: 0, 2: 1}


# 31120kb, 44ms
def sol2(n):
    if n in d:
        return d[n]
    t = 1 + min(sol2(n // 3) + n % 3, sol2(n // 2) + n % 2)
    d[n] = t
    return t


if __name__ == "__main__":
    n = int(input())
    print(sol2(n))
