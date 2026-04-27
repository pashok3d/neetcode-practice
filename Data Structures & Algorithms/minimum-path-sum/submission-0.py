from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows_n = len(grid)
        cols_n = len(grid[0])
        @lru_cache
        def dp(row, column):
            if row == rows_n-1 and column == cols_n-1:
                return grid[row][column]
            if row > rows_n-1 or column > cols_n-1:
                return 201
            return grid[row][column] + min(dp(row+1, column), dp(row, column+1))

        return dp(0, 0)