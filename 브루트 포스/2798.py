# 블랙잭
from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cmbnt = combinations(nums, 3)
blackjack = 0
for c in cmbnt:
    s = sum(c)
    if blackjack < s <= m:
        blackjack = s
print(blackjack)