class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1,j)
            dfs(i, j-1)

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    count += 1
        
        return count
        
        