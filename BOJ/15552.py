# 빠른 A + B
import sys

n = int(sys.stdin.readline().rstrip())  # 이건 input으로 해도
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
