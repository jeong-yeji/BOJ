def sol1(a, b):
    prefix = [0]
    n = m = 0
    for _ in range(b):
        if n == m:
            n += 1
            m = 0
        prefix.append(prefix[-1] + n)
        m += 1
    return prefix[b] - prefix[a - 1]


def sol2(a, b):
    l = [i for i in range(50) for j in range(i)]
    return sum(l[a - 1:b])


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(sol1(n, m))
    print(sol2(n, m))
