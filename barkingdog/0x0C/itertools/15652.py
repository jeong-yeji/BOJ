from itertools import combinations_with_replacement

n, m = map(int, input().split())
print("\n".join(list(map(' '.join, combinations_with_replacement(map(str, range(1, n + 1)), m)))))
