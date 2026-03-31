class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = None
        profit = 0
        for price in prices:
            if min_seen is None:
                min_seen = price
                continue
            elif price < min_seen:
                min_seen = price
            elif price > min_seen:
                profit = max(profit, price - min_seen)

        return profit