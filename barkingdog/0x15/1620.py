import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
l = [input() for _ in range(n)]
d = {v: str(i) for i, v in enumerate(l, 1)}
q = [input() for _ in range(m)]
print('\n'.join(l[int(i) - 1] if i.isdigit() else d[i] for i in q))
