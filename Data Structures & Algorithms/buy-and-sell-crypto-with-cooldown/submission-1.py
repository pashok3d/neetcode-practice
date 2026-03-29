from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i_day, can_buy):
            if i_day >= len(prices):
                return 0
            if can_buy:
                return max(dp(i_day + 1, False) - prices[i_day], dp(i_day + 1, True))
            else:
                return max(dp(i_day + 1, False), dp(i_day + 2, True) + prices[i_day])

        return dp(0, True)

            