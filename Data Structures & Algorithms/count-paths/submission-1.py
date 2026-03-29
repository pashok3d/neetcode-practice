class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[n-1][m-1] = 1
        
        # populate dp
        for y in range(n-1, -1, -1):
            for x in range(m-1, -1, -1):
                if x == m - 1 and y == n - 1:
                    pass
                elif x == m - 1:
                    dp[y][x] = dp[y+1][x]
                elif y == n - 1:
                    dp[y][x] = dp[y][x+1]
                else:
                    dp[y][x] = dp[y][x+1] + dp[y+1][x]

        return dp[0][0]