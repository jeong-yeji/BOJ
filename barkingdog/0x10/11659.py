import itertools
import sys

input = lambda: sys.stdin.readline().strip()


def prefix1(numbers):
    prefix_sum = [0]
    for i in range(len(numbers)):
        prefix_sum.append(prefix_sum[-1] + numbers[i])
    return prefix_sum


def prefix2(numbers):
    return list(itertools.accumulate(numbers, initial=0))


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# prefix_sum = prefix1(numbers)
prefix_sum = prefix2(numbers)

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
