import sys

input = lambda: sys.stdin.readline().strip()

k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]

s, e = 1, 2 ** 31 - 1
while s < e:
    mid = (s + e + 1) // 2
    if sum(wire // mid for wire in wires) >= n:
        s = mid
    else:
        e = mid - 1
print(s)
