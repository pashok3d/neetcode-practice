class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        cols = len(grid[0])
        rows = len(grid)
        visited = set()

        def dfs(y, x):
            if (y, x) in visited:
                return
            if y >= rows:
                return
            if x >= cols:
                return 
            if y < 0 or x < 0:
                return
            if grid[y][x] == "0":
                return

            visited.add((y, x))

            dfs(y+1, x)
            dfs(y, x+1)
            dfs(y-1, x)
            dfs(y, x-1)

            return

        for r_i, r in enumerate(grid):
            for c_i, c in enumerate(r):
                if c == "1" and (r_i,c_i) not in visited:
                    counter += 1
                    dfs(r_i, c_i)

        return counter

        