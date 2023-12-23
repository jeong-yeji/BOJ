from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
print("\n".join(list(map(' '.join, combinations_with_replacement(map(str, numbers), m)))))
