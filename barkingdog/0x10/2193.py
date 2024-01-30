def sol1(n):
    dp = [[0, 1]]
    for i in range(1, n):
        dp.append([sum(dp[-1]), dp[-1][0]])
    return sum(dp[-1])


def sol2(n):
    z, o = 0, 1
    for _ in range(n - 1):
        z, o = z + o, z
    return z + o


if __name__ == "__main__":
    n = int(input())
    print(sol1(n))
    print(sol2(n))
