from itertools import combinations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for combination in combinations(numbers, m):
    print(*combination)
