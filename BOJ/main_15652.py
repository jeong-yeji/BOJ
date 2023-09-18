n, m = map(int, input().split())
arr = []


def recur(k, l):
    if k == m:
        print(*arr)
        return
    for i in range(l, n + 1):
        arr.append(i)
        recur(k + 1, i)
        arr.pop()


recur(0, 1)
