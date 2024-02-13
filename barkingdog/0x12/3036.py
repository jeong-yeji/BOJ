import math

n = int(input())
r, *rings = list(map(int, input().split()))
for ring in rings:
    d = math.gcd(r, ring)
    print(r // d, ring // d, sep="/")
