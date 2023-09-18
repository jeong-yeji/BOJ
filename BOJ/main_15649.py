n, m = map(int, input().split())
arr = []


def recur(k):
    if k == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            recur(k + 1)
            arr.pop()


recur(0)
