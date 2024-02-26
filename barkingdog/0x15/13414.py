import sys

input = lambda: sys.stdin.readline().strip()

k, l = map(int, input().split())
lines = {input(): i for i in range(l)}
print('\n'.join(k for k, v in sorted(lines.items(), key=lambda x: x[1])[:k]))
