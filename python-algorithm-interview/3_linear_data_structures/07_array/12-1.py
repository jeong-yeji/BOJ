# best-time-to-buy-and-sell-stock

import sys


class Solution:
    # 저점과 현재 값과의 차이 계산
    def maxProfit(self, prices) -> int:
        profit = 0  # -sys.maxsize로 설정하면 빈 배열을 입력받는 경우 오류 발생, 최대값은 0보다 커야됨
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)  # 저점 갱신
            profit = max(profit, price - min_price)  # 저점과 현재 값의 차이 vs 현재 수익

        return profit
