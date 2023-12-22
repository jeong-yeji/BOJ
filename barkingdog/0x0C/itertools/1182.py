import sys
from itertools import combinations

input = lambda: sys.stdin.readline().strip()

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
res = 0
for i in range(1, n + 1):
    for combi in combinations(numbers, i):
        if sum(combi) == s:
            res += 1
print(res)
