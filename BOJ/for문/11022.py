# A + B
import sys

for i in range(1, int(input()) + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")
