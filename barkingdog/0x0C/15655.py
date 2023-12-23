n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []
vis = [False] * n


def recur(idx):
    global n, m
    if len(res) == m:
        print(*res)
        return

    for i in range(idx, n):
        if not vis[i]:
            vis[i] = True
            res.append(numbers[i])
            recur(i + 1)
            vis[i] = False
            res.pop()


recur(0)
