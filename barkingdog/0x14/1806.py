import sys

n, m = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
s, e, total, answer = 0, 0, numbers[0], n + 1
while True:
    if total >= m:
        answer = min(answer, e - s + 1)
        total -= numbers[s]
        s += 1
    else:
        e += 1
        if e < n:
            total += numbers[e]
        else:
            break
print(0 if answer > n else answer)
