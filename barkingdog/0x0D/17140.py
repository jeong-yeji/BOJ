from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
while True:
    if r - 1 < len(arr) and c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        print(time)
        break

    if time > 100:
        print(-1)
        break
    time += 1

    lr, lc = len(arr), max(map(len, arr))

    if lr < lc:
        arr = list(zip(*arr))

    for idx, val in enumerate(arr):
        count = sorted(Counter(filter(lambda x: x != 0, val)).most_common(), key=lambda x: (x[1], x[0]))[:50]
        arr[idx] = [col for row in count for col in row]

    maxlen = max(map(len, arr))
    for idx, val in enumerate(arr):
        arr[idx] = val + [0] * (maxlen - len(val))

    if lr < lc:
        arr = list(zip(*arr))
