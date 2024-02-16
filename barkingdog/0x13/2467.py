def sol1(n, liquids):
    liquids.sort()

    if liquids[0] >= 0:
        return liquids[:2]
    elif liquids[-1] <= 0:
        return liquids[-2:]

    l, r, ans = 0, n - 1, abs(liquids[0] + liquids[n - 1])
    s, e = 0, n - 1
    while s < e:
        tmp = liquids[s] + liquids[e]
        if abs(tmp) < ans:
            l, r, ans = s, e, abs(tmp)
            if tmp == 0:
                break
        if tmp < 0:
            s += 1
        else:
            e -= 1
    return liquids[l], liquids[r]


def sol2(n, liquids):
    liquids.sort(key=lambda x: abs(x))
    idx, tmp = 0, abs(liquids[0] + liquids[1])
    for i in range(1, n - 1):
        if abs(liquids[i] + liquids[i + 1]) < tmp:
            idx, tmp = i, abs(liquids[i] + liquids[i + 1])
    return sorted([liquids[idx], liquids[idx + 1]])


if __name__ == "__main__":
    n = int(input())
    liquids = list(map(int, input().split()))
    print(*sol1(n, liquids))
    print(*sol2(n, liquids))
