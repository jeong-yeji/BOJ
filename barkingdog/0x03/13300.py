import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * 2 for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    arr[y][s] += 1

cnt = 0
for g, b in arr:
    cnt += math.ceil(g / k)
    cnt += math.ceil(b / k)
print(cnt)
