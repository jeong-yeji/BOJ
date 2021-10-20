# best-time-to-buy-and-sell-stock
# 풀어보려고 시도했으나 시간 초과로 풀리지 않음..


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices)):
            profit = max(max(prices[i:]) - prices[i], profit)
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
