import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

cnt = [0] * m

prefix_sum = [nums[0]]
for num in nums[1:]:
    prefix_sum.append(prefix_sum[-1] + num)

for i in range(n):
    remain = prefix_sum[i] % m
    cnt[remain] += 1
    if remain == 0:
        res += 1

for c in cnt:
    if c > 1:
        res += c * (c - 1) // 2

print(res)
