def eratos(n):
    prime = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return prime


def sol1(n):
    if n == 1:
        return 0

    prime = eratos(n)
    s, e, cnt, cur = 0, 0, 0, prime[0]
    while True:
        if cur < n:
            e += 1
            if e < len(prime):
                cur += prime[e]
            else:
                break
        else:
            if cur == n:
                cnt += 1
            cur -= prime[s]
            s += 1
    return cnt


def sol2(n):
    if n == 1:
        return 0

    prime = eratos(n)
    s = cur = cnt = 0
    for e in prime:
        cur += e
        while cur > n:
            cur -= prime[s]
            s += 1
        if cur == n:
            cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    print(sol1(n))
    print(sol2(n))
