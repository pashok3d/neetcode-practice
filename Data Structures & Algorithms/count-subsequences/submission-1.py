from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # top-down approach try
        # lets use some index-based pointers
        # i for s
        # j for t

        # intuition: number of 
        # distinct subseqences of "caaat" that are equal to "cat"
        # should be 1 + number of distinct subsequences of "aaat" that are equal to "at"

        # where number of distinct subsequences of "aaat" that are equal to "at"
        # "aa(at)"
        # "a(a)a(t)"
        # "(a)aa(t)"

        @lru_cache
        def dp(i, j) -> int:
            # dp at i, j should be smth like "number of distinct subsequences of s[i:] that are equal to t[j:]"
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0


            if s[i] == t[j]:
                return dp(i+1, j+1) + dp(i+1, j)
            else:
                return dp(i+1, j)
                
                
        return dp(0, 0)