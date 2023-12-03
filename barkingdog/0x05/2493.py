import sys

n = int(input())
towers = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0] * n
stack = []

for idx, val in enumerate(towers):
    while stack:
        if stack[-1][1] > val:
            result[idx] = stack[-1][0]
            break
        stack.pop()
    stack.append([idx + 1, val])

print(*result)
