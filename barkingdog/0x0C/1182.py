import sys

input = lambda: sys.stdin.readline().strip()

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
res = 0


def recur(idx, cur):
    global s, res
    if idx == n:
        if cur == s:
            res += 1
        return

    recur(idx + 1, cur)
    recur(idx + 1, cur + numbers[idx])


recur(0, 0)
print(res - 1 if s == 0 else res)
