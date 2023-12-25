from itertools import product

n, m = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
print("\n".join(list(map(' '.join, product(map(str, numbers), repeat=m)))))
