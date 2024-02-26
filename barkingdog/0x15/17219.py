import sys

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
d = {}
for _ in range(n):
    url, pw = input().split()
    d[url] = pw
print('\n'.join(d[input()] for _ in range(m)))
