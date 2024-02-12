def sol1(E, S, M):
    e = s = m = y = 1
    while True:
        if E == e and S == s and M == m:
            return y
        e += 1
        s += 1
        m += 1
        y += 1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1


def sol2(e, s, m):
    y = 1
    while (y - e) % 15 or (y - s) % 28 or (y - m) % 19:
        y += 1
    return y


if __name__ == "__main__":
    e, s, m = map(int, input().split())
    print(sol1(e, s, m))
    print(sol2(e, s, m))
