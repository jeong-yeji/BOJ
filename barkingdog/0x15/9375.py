import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    clothes = defaultdict(int)
    for j in range(int(input())):
        clothes[input().split()[1]] += 1
    answer = 1
    for v in clothes.values():
        answer *= v + 1
    print(answer - 1)
