from itertools import combinations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
print("\n".join(list(map(' '.join, combinations(map(str, numbers), m)))))
