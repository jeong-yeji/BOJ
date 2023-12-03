import sys

stack = []
res = []
i = 0

for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())

    while i < n:
        i += 1
        stack.append(i)
        res.append("+")

    if stack[-1] == n:
        stack.pop()
        res.append('-')
    else:
        res.append('NO')
        break

print("NO" if "NO" in res else "\n".join(res))
