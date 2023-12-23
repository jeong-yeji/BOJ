from itertools import product

n, m = map(int, input().split())
print("\n".join(list(map(' '.join, product(map(str, range(1, n + 1)), repeat=m)))))
