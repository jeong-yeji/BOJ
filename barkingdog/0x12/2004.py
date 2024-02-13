def count2(n):
    cnt = 0

    # 1 : n // 2 + n // 4 + n // 8 + ...
    while n >= 2:
        cnt += n // 2
        n //= 2

    # 2
    # while n:
    #     n //= 2
    #     cnt += n

    return cnt


def count5(n):
    cnt = 0

    # 1 : n//5 + n//25 + n//125 +...
    while n >= 5:
        cnt += n // 5
        n //= 5

    # 2
    # while n:
    #     n //= 5
    #     cnt += n
    
    return cnt


n, m = map(int, input().split())
cnt2 = count2(n) - count2(n - m) - count2(m)
cnt5 = count5(n) - count5(n - m) - count5(m)
print(min(cnt2, cnt5))
