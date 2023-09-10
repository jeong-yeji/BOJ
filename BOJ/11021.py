# A + B
import sys

n = int(input())
for i in range(1, n + 1):  # for i in range(1, int(input())+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a+b}")
