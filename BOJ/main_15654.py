n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
arr = []


def recur(k):
    if k == m:
        print(*arr)
        return
    for i in range(n):
        if numbers[i] not in arr:
            arr.append(numbers[i])
            recur(k + 1)
            arr.pop()


recur(0)
