n, m = map(int, input().split())
res = []


def recur(depth, idx):
    global n, m
    if depth == m:
        print(*res)
        return

    for i in range(idx, n + 1):
        res.append(i)
        recur(depth + 1, i)
        res.pop()


recur(0, 1)
