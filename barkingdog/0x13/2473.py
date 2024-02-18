def sol1(n, liquids):
    if liquids[0] >= 0:
        return liquids[:3]
    elif liquids[-1] <= 0:
        return liquids[-3:]

    a, b, c = 0, n // 2, n - 1
    ans = abs(liquids[a] + liquids[b] + liquids[c])

    for s in range(n - 2):
        m, e = s + 1, n - 1
        while m < e:
            tmp = liquids[s] + liquids[m] + liquids[e]
            if abs(tmp) < ans:
                a, b, c, ans = s, m, e, abs(tmp)
                if ans == 0:
                    break
            if tmp < 0:
                m += 1
            else:
                e -= 1
        if ans == 0:
            break
    return liquids[a], liquids[b], liquids[c]


if __name__ == "__main__":
    n = int(input())
    liquids = sorted(map(int, input().split()))
    print(*sol1(n, liquids))
