n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []


def recur(depth, idx):
    global n, m
    if depth == m:
        print(*res)
        return

    prev = 0
    for i in range(idx, n):
        if numbers[i] != prev:
            res.append(numbers[i])
            prev = numbers[i]
            recur(depth + 1, i)
            res.pop()


recur(0, 0)
