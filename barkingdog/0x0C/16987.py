import sys

input = lambda: sys.stdin.readline().strip()


def recur(cur, cnt):
    global n, res
    if cur == n:
        res = max(res, cnt)
        return

    target = eggs[cur]
    if target[0] <= 0:
        recur(cur + 1, cnt)
        return

    if cnt == n - 1:
        res = max(res, cnt)
        return

    for idx, egg in enumerate(eggs):
        if egg[0] <= 0 or idx == cur:
            continue
        target[0] -= egg[1]
        egg[0] -= target[1]
        tmp = 0
        tmp += target[0] <= 0
        tmp += egg[0] <= 0
        recur(cur + 1, cnt + tmp)
        target[0] += egg[1]
        egg[0] += target[1]


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
res = 0
recur(0, 0)
print(res)
