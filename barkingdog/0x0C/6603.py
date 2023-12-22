def recur(cur, i):
    global n
    if cur == 6:
        print(*res)
        return

    for i in range(i, n):
        res.append(numbers[i])
        recur(cur + 1, i + 1)
        res.pop()


while True:
    n, *numbers = list(map(int, input().split()))
    if n == 0:
        break
    res = []
    recur(0, 0)
    print()
