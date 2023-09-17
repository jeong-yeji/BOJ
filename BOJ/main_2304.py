import sys

input = sys.stdin.readline

sticks = [0] * 1001
max_idx, max_val = 0, 0
for _ in range(int(input())):
    idx, val = map(int, input().split())
    sticks[idx] = val
    if val > max_val:
        max_idx, max_val = idx, val

answer = max_val


def calc(vals):
    curr = 0
    for val in vals:
        global answer
        answer += curr
        if val > curr:
            curr = val


calc(sticks[:max_idx + 1])
calc(sticks[1001:max_idx - 1:-1])

print(answer)
