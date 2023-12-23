from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
print("\n".join(list(map(' '.join, permutations(map(str, numbers), m)))))
