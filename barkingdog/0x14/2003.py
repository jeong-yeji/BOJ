def sol1(n, m, numbers):
    s = e = cnt = 0
    cur = numbers[0]
    while True:
        if cur < m:
            e += 1
            if e < n:
                cur += numbers[e]
            else:
                break
        else:
            if cur == m:
                cnt += 1
            cur -= numbers[s]
            s += 1
    return cnt


def sol2(n, m, numbers):
    s = cur = cnt = 0
    for e in numbers:
        cur += e
        while cur > m:
            cur -= numbers[s]
            s += 1
        if cur == m:
            cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(sol1(n, m, numbers))
    print(sol2(n, m, numbers))
