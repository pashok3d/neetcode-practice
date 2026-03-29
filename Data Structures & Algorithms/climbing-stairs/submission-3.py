from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def ways(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return ways(n-1) + ways(n-2)

        return ways(n)

        