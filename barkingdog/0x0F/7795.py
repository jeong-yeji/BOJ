import sys

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    n, m = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    cnt, idx = 0, 0
    for a in A:
        while idx < m and B[idx] < a:
            idx += 1
        cnt += idx
    print(cnt)
