n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []
vis = [False] * n


def recur(depth, idx):
    global n, m
    if depth == m:
        print(*res)
        return

    prev = 0
    for i in range(idx, n):
        if not vis[i] and numbers[i] != prev:
            res.append(numbers[i])
            vis[i] = True
            prev = numbers[i]
            recur(depth + 1, i)
            res.pop()
            vis[i] = False


recur(0, 0)
