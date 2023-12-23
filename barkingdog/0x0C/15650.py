n, m = map(int, input().split())
res = []
vis = [False] * (n + 1)


def recur(idx):
    global n, m
    if len(res) == m:
        print(*res)
        return

    for i in range(idx, n + 1):
        if not vis[i]:
            vis[i] = True
            res.append(i)
            recur(i + 1)
            vis[i] = False
            res.pop()


recur(1)
