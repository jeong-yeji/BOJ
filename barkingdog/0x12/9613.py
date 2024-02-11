import itertools
import math

for _ in range(int(input())):
    print(sum(math.gcd(a, b) for a, b in itertools.combinations(list(map(int, input().split()))[1:], 2)))
