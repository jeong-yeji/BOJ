n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = []


def recur(depth):
    global n, m
    if depth == m:
        print(*res)
        return

    prev = 0
    for i in range(n):
        if numbers[i] != prev:
            res.append(numbers[i])
            prev = numbers[i]
            recur(depth + 1)
            res.pop()


recur(0)
