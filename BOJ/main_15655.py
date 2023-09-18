n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
arr = []


def recur(k, l):
    if k == m:
        print(*arr)
        return
    for i in range(l, n):
        if numbers[i] not in arr:
            arr.append(numbers[i])
            recur(k + 1, i + 1)
            arr.pop()


recur(0, 0)
