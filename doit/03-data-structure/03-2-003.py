import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum, res = [0], []

for i in range(len(nums)):
    prefix_sum.append(prefix_sum[-1] + nums[i])

for _ in range(m):
    start, end = map(int, input().split())
    res.append(prefix_sum[end] - prefix_sum[start - 1])

for r in res:
    print(r)