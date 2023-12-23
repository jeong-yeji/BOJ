n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []
vis = [False] * n


def recur(depth):
    global n, m
    if depth == m:
        print(*res)
        return

    for i in range(n):
        if not vis[i]:
            res.append(numbers[i])
            vis[i] = True
            recur(depth + 1)
            res.pop()
            vis[i] = False


recur(0)
