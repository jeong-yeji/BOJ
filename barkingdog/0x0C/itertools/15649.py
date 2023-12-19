from itertools import permutations

n, m = map(int, input().split())
print("\n".join(map(' '.join, permutations(map(str, range(1, n + 1)), m))))
