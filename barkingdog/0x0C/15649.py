n, m = map(int, input().split())
arr, vis = [0] * 10, [0] * 10


def recur(k):
    global n, m
    if k == m:
        print(*arr[:m])

    for i in range(1, n + 1):
        if not vis[i]:
            arr[k] = i
            vis[i] = True
            recur(k + 1)
            vis[i] = False


recur(0)
