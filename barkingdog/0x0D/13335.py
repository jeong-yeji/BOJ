import sys

input = lambda: sys.stdin.readline().strip()
n, w, L = map(int, input().split())
weights = list(map(int, input().split()))
time = [0] * (1000 * 100)
answer, cur = 0, 0
for weight in weights:
    while time[cur] + weight > L:
        cur += 1
    for i in range(cur, cur + w):
        time[i] += weight
    cur += 1
print(cur + w)
