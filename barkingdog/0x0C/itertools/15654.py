from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for permutation in permutations(numbers, m):
    print(*permutation)
