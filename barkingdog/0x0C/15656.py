n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []


def recur(depth, idx):
    global n, m
    if depth == m:
        print(*res)
        return

    for i in range(n):
        res.append(numbers[i])
        recur(depth + 1, i)
        res.pop()


recur(0, 0)
