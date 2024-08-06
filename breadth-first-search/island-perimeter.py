class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check all four possible directions
                    # Check up
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    # Check down
                    if r == rows-1 or grid[r+1][c] == 0:
                        perimeter += 1
                    # Check left
                    if c == 0 or grid[r][c-1] == 0:
                        perimeter += 1
                    # Check right
                    if c == cols-1 or grid[r][c+1] == 0:
                        perimeter += 1

        return perimeter