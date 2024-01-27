import sys

cnt = [0] * 10001
for _ in range(int(input())):
    cnt[int(sys.stdin.readline().strip())] += 1
for i in range(10001):
    for _ in range(cnt[i]):
        sys.stdout.write(f'{i}\n')
