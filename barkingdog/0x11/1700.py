n, k = map(int, input().split())
use = list(map(int, input().split()))
code = []
answer = 0

for i in range(k):
    if use[i] in code:
        continue

    if len(code) < n:
        code.append(use[i])
        continue

    target, val = -1, -1
    for c in code:
        if c in use[i:]:
            idx = use[i:].index(c)
            if idx > val:
                target, val = c, idx
        else:
            target, val = c, 101
            break
    code.remove(target)
    code.append(use[i])
    answer += 1

print(answer)
