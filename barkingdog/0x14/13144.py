def sol1(n, numbers):
    s = e = ans = 0
    vis = [False] * 100001
    while s < n and e < n:
        if vis[numbers[e]]:
            while vis[numbers[e]]:
                vis[numbers[s]] = False
                s += 1
        else:
            vis[numbers[e]] = True
            e += 1
            ans += e - s
    return ans


def sol2(n, numbers):
    e = ans = 0
    vis = [False] * 100001
    for s in range(n):
        while e < n:
            if vis[numbers[e]]:
                break
            vis[numbers[e]] = True
            e += 1
        ans += e - s
        vis[numbers[s]] = False
    return ans


def sol3(n, numbers):
    dic = {}
    pre = -1
    ans = 0
    for i, v in enumerate(numbers):
        if v in dic:
            pre = max(pre, dic[v])
        dic[v] = i
        ans += i - pre
    return ans


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(sol1(n, numbers))
    print(sol2(n, numbers))
    print(sol3(n, numbers))
