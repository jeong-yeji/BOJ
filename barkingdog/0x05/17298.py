import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        res[stack.pop()] = arr[i]
    stack.append(i)

print(*res)
