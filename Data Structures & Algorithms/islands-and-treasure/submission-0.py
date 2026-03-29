from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        q = deque()

        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if cell == 0:
                    # add to bfs deque
                    q.append((row_i, col_i, 0))

        while q:
            row_i, col_i, path = q.popleft()
            
            for row_i_next, col_i_next in [(row_i-1, col_i), (row_i+1, col_i), (row_i, col_i-1), (row_i, col_i+1)]:
                if row_i_next < 0 or col_i_next < 0 or row_i_next >= m or col_i_next >= n:
                    continue
                if grid[row_i_next][col_i_next] == INF:
                    grid[row_i_next][col_i_next] = path + 1
                    q.append((row_i_next, col_i_next, path+1))
            

        


