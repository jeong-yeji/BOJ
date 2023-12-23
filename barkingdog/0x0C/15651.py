n, m = map(int, input().split())
res = []


def recur(idx):
    global n, m
    if len(res) == m:
        print(*res)
        return

    for i in range(1, n + 1):
        res.append(i)
        recur(i + 1)
        res.pop()


recur(1)
