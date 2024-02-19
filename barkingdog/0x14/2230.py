def sol1(n, m, a):
    s, e, answer = 0, 0, a[-1] - a[0]
    while e < n:
        tmp = a[e] - a[s]
        if tmp == m:
            return m
        elif tmp > m:
            answer = min(answer, tmp)
            s += 1
        else:
            e += 1
    return answer


def sol2(n, m, a):
    e, answer = 0, a[-1] - a[0]
    for s in range(n):
        while e < n and a[e] - a[s] < m:
            e += 1
        if e == n:
            break
        answer = min(answer, a[e] - a[s])
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a.sort()
    print(sol1(n, m, a))
    print(sol2(n, m, a))
